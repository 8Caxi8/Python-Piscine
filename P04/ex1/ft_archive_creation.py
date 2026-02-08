def preservation_system() -> None:
    FILE_NAME: str = "new_discovery.txt"
    TEXT: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist dansimoe\n",
    ]

    try:
        print(f"Initializing new storage unit: {FILE_NAME}")
        with open(FILE_NAME, "w") as file:
            print("Storage unit created successfully...")
            print()
            print("Inscribing preservation data...")
            for line in TEXT:
                file.write(line)
                print(line, end="")
            print()
    except OSError as e:
        print(f"Storage vault error: {e}.")
        print()
        return

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{FILE_NAME}' ready for long-term preservation.")


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    preservation_system()


if __name__ == "__main__":
    main()
