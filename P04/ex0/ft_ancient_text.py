def recovery_system() -> None:
    file_name: str = "ancient_fragment.txt"

    try:
        print(f"Accessing Storage Vault: {file_name}")
        with open(file_name, "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
            print()
    except OSError:
        print("ERROR: Storage vault not found.\n")
        return

    print("Data recovery complete. Storage unit disconnected.\n")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    recovery_system()


if __name__ == "__main__":
    main()
