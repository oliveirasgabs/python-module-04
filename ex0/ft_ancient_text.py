import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {filename}")

    file_handle: IO[str] | None = None
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
