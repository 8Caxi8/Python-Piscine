class SecurePlant:
    def __init__(self, name: str, height: [int | None] = None, age: [int | None] = None) -> None:
        if height < 0:
            return print("Security: Negative height rejected")
        elif age < 0:
            return print("Security: Negative age rejected")
        self.age = age
        self.name = name
        self.growth = 0
        print(f"Plant created: {self.name} ({self.height}cm, {self.age} days)")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int = 1) -> None:
        self.height += growth
        self.growth += growth

    def set_age(self, age: int = 1) -> None:
        self.age += age


print("=== Garden Security System ===")

rose: SecurePlant = ["Rose", 10, 10]
rose.get_info()
