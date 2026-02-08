import sys


def command_quest() -> None:
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")

        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")


def main() -> None:
    print("=== Command Quest ===")
    command_quest()
    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()
