def preservation() -> None:
    file_name: str = "security_protocols.txt"
    protocols: str = "[CLASSIFIED] New security protocols archived"

    try:
        with open(file_name, "w") as file:
            print("SECURE PRESERVATION:")
            file.write(protocols)
            print(protocols)

    except OSError as e:
        print(f"Storage vault error: {e}.\n")

    print("Vault automatically sealed upon completion\n")


def extraction() -> None:
    file_name: str = "classified_data.txt"

    try:
        with open(file_name) as file:
            print("Vault connection established with failsafe protocols\n")

            print("SECURE EXTRACTION:")
            print(file.read())
            print()
    except OSError as e:
        print(f"Storage vault error: {e}.\n")


def main() -> None:
    print("CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    extraction()
    preservation()

    print("All vault operations completed with maximim security.\n")


if __name__ == "__main__":
    main()
