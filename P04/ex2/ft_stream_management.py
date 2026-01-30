import sys


def std_in() -> list[str]:
    arch_id: str
    status_report: str

    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    arch_id = sys.stdin.readline().rstrip("\n")
    if not arch_id:
        print("Error: No archivist ID received!\n")
        return []

    status_report = input("Input Stream active. Enter status report: ")
    if not status_report:
        print("Error: No status report received!\n")
        return []
    return [status_report, arch_id]


def std_out(arch_status: list[str]) -> None:
    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_status[1]}: "
                     f"{arch_status[0]}\n")
    std_err()

    sys.stdout.write("[STANDARD] Data transmission complete\n")


def std_err() -> None:
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    std_out(std_in())

    print()
    print("Three-channel communication test successful\n")


if __name__ == "__main__":
    main()
