def preservation_system() -> None:
    file_name: str = "new_discovery.txt"
    text: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist dansimoe\n",
    ]

    try:
        print(f"Initializing new storage unit: {file_name}")
        with open(file_name, "w") as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            for line in text:
                file.write(line)
                print(line, end="")
            print()
    except OSError as e:
        print(f"Storage vault error: {e}.\n")
        return

    print("Data inscription complete. Storage unit sealed")
    print(f"Archive '{file_name}' ready for long-term preservation.")


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    preservation_system()


if __name__ == "__main__":
    main()
