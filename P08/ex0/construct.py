import sys
import os


def inside_matrix() -> None:
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install.\n")

    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\n"
          "Scripts\n"
          "activate    # On Windows\n")

    print("Then run this program again.")


def outside_matrix() -> None:
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting the global system.\n")

    print("Package installation path:")
    print("")


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        inside_matrix()
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        outside_matrix()


if __name__ == "__main__":
    main()
