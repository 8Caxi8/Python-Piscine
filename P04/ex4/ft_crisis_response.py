SYSTEM = "system"
SECURITY = "security"
CORRUPTED = "corrupted"
STANDARD = "standard"


def access_file(file_name: str) -> str:

    try:
        with open(file_name, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            data = file.read().strip()

    except FileNotFoundError:
        crisis_alert(file_name)
        print("RESPONSE: Archive not found in storage matrix")
        return SYSTEM

    except PermissionError:
        crisis_alert(file_name)
        print("RESPONSE: Security protocols deny access")
        return SECURITY

    except OSError:
        crisis_alert(file_name)
        print("RESPONSE: Security measures in place")
        return CORRUPTED

    print(f"SUCCESS: Archive recovered - \"{data}\"")
    return STANDARD


def crisis_alert(file_name: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")


def crisis_handler(file_name: str) -> None:
    status = access_file(file_name)
    match status:
        case "system":
            print("STATUS: Crisis handled, system stable\n")
        case "security":
            print("STATUS: Crisis handled, security maintained\n")
        case "corrupted":
            print("STATUS: Crisis handled, corruption denied\n")
        case "standard":
            print("STATUS: Normal operations resumed\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
