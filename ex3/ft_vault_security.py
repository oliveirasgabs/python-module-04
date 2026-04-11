def secure_archive(file_name: str, action: str,
                   content: str = "") -> tuple[bool, str]:
    try:
        if (action == "r"):
            with open(file_name, action) as file_handle:
                print(f"Using '{file_name}' to read from a regular file")
                return (True, file_handle.read())

        elif (action == "w"):
            with open(file_name, action) as file_handle:
                print(f"Using '{file_name}' to write "
                      f"previous content to a new file")
                file_handle.write(content)
                return (True, "Content successfully written to file")

    except FileNotFoundError as error:
        print(f"Using '{file_name}' to read from a nonexistent file:")
        return (False, f"{error}")
    except PermissionError as error:
        print(f"Using '{file_name}' to read from an inaccessible file:")
        return (False, f"{error}")
    except OSError as error:
        return (False, f"{error}")
    return (False, "Please, inform if you want read <r> or write <w>")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print(secure_archive("non_exist.txt", "r"))
    print("\n")
    print(secure_archive("permission_denied", "r"))
    print("\n")
    existing: tuple[bool, str] = secure_archive("new2.txt", "r")
    print(existing)
    print("\n")
    print(secure_archive("new_file.txt", "w", existing[1]))


if __name__ == "__main__":
    main()
