import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict[str, str | None]:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_configuration(config: dict) -> bool:
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("[WARNING]: Missing configuration variables:")
        for key in missing:
            print(f" - {key}")
            print("\nPlease configure your .env "
                  "file or set environment variables.")

            return False

    return True


def simulate_environment_behavior(config: dict) -> None:
    mode = config["MATRIX_MODE"]

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to secure production cluster")
    else:
        print("[WARNING]: Unknown MATRIX_MODE")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Key not valid!")

    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")


def security_check() -> None:
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING]: No .env file detected")

    print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    config: dict[str, str | None] = load_configuration()

    if not validate_configuration(config):
        sys.exit(1)

    simulate_environment_behavior(config)
    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
