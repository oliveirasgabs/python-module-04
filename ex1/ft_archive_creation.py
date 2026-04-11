import sys
from typing import IO

# The following standard types and collections are allowed, along with
# all their associated methods and constructors: str, int, float,
# list, dict, set, tuple.

# Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
# io.read(), io.write(), io.close(), print(), input()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    content: str = ""

    print("=== Cyber Archives Recovery & Preservation ===")
    file_handle: IO[str] | None = None
    try:
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Accessing file '{filename}'")
        print("---\n")
        print(content, end="")
        print("\n---")
    except FileNotFoundError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
        return
    except PermissionError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
        return
    except OSError as error:
        print(f"Error opening file '{filename}': "
              f"{error}")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{filename}' closed.\n")

    print("Transform data:")
    print("\n---")
    lines: list[str] = content.splitlines()
    new_content: str = "\n".join([line + "#" for line in lines]) + "\n"
    print(new_content, end="")
    print("---")

    save_name: str = input("Enter new file name (or empty): ")
    if not save_name:
        print("Not saving data.")
        return

    file_w: IO[str] | None = None
    try:
        print(f"Saving data to '{save_name}'")
        file_w = open(save_name, 'w')
        file_w.write(new_content)
    except OSError as error:
        print(f"Error saving file '{save_name}': "
              f"{error}")
    finally:
        if file_w is not None:
            file_w.close()


if __name__ == "__main__":
    main()
