class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return

        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return

        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def get_info(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    rose: SecurePlant = SecurePlant("Rose", 25, 30)
    rose.get_info()
    print()
    rose.set_height(-5)
    print()
    rose.get_info()


if __name__ == "__main__":
    main()
