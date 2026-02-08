def recovery_system() -> None:
    FILE_NAME: str = "ancient_fragment.txt"

    try:
        print(f"Accessing Storage Vault: {FILE_NAME}")
        with open(FILE_NAME, "r") as file:
            print("Connection established...")
            print()
            print("RECOVERED DATA:")
            print(file.read())
            print()
    except OSError:
        print("ERROR: Storage vault not found. "
              "Run data generator first.")
        print()
        return

    print("Data recovery complete. Storage unit disconnected.")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    recovery_system()


if __name__ == "__main__":
    main()
