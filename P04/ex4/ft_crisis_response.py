def file_not_found() -> None:
    file_name: str = "lost_archive.txt"

    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        open(file_name, "r")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")

    print("STATUS: Crisis handled, system stable\n")


def restricted_access() -> None:
    file_name: str = "classified_data.txt"

    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        open(file_name, "w")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")

    print("STATUS: Crisis handled, security maintained\n")


def standard_archive() -> None:
    file_name: str = "standard_archive.txt"

    print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    try:
        file = open(file_name, "r")
        print(f"SUCCESS: Archive recovered - {file.read()}")
    except OSError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security breached")

    print("STATUS: Normal operations resumed\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_not_found()

    restricted_access()

    standard_archive()

    print("All crisis scenarios handled successfully. Archives secure.\n")


if __name__ == "__main__":
    main()
