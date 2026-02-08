import sys


class VaultError(Exception):
    pass


def std_in() -> tuple[str, str]:
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    arch_id = sys.stdin.readline().rstrip("\n")
    if not arch_id:
        raise VaultError("Error: No archivist ID received!\n")

    status_report = input("Input Stream active. Enter status report: ")
    if not status_report:
        raise VaultError("Error: No status report received!\n")

    return status_report, arch_id


def std_out(status_report: str, arch_id: str) -> None:
    sys.stdout.write(f"[STANDARD] Archive status from {arch_id}: "
                     f"{status_report}\n")
    std_err()

    sys.stdout.write("[STANDARD] Data transmission complete\n")


def std_err() -> None:
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    try:
        status_report, arch_id = std_in()
        print()
        std_out(status_report, arch_id)
        print()
        print("Three-channel communication test successful")
    except VaultError as e:
        sys.stderr.write(str(e))


if __name__ == "__main__":
    main()
