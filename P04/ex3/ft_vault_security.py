def preservation() -> None:
    FILE_NAME: str = "security_protocols.txt"
    PROTOCOLS: str = "[CLASSIFIED] New security protocols archived"

    try:
        with open(FILE_NAME, "w") as file:
            print("SECURE PRESERVATION:")
            file.write(PROTOCOLS)
            print(PROTOCOLS)

        if not file.closed:
            print("Sorage vault was not correctly sealed!\n")

    except OSError as e:
        print(f"Storage vault error: {e}.\n")

    finally:
        print("Vault automatically sealed upon completion\n")


def extraction() -> None:
    FILE_NAME: str = "classified_data.txt"

    print("Vault connection established with failsafe protocols\n")
    try:
        with open(FILE_NAME) as file:
            print("SECURE EXTRACTION:")
            print(file.read())
            print()
    except OSError as e:
        print(f"Storage vault error: {e}.\n")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()

    print("Initiating secure vault access...")
    extraction()
    preservation()

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
