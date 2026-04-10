import sys
from typing import IO

# I can only use Authorized:
# import sys, sys.argv, len(), open(), import typing, typing.IO, io.read(),
# io.close(), print()#

# Its authorized: The following standard types and collections are allowed,
# along with all their associated methods and constructors:
# str, int, float, list, dict, set, tuple.


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {filename}")

    file_handle: IO | None = None
    try:
        file_handle = open(filename, 'r')
        content: str = file_handle.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except FileNotFoundError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
    except PermissionError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
    except OSError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
