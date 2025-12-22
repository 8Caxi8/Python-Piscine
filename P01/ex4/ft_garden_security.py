class SecurePlant:
    def secure_create(self, height: int, age: int) -> int:
        if height < 0:
            return (print("Security: Negative height rejected"), 0)
        elif age < 0:
            return (print("Security: Negative age rejected"), 0)
        else:
            self.set_age(age)
            self.set_height(height)

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int = 1) -> None:
        self.height += growth
        self.growth += growth

    def set_age(self, age: int = 1) -> None:
        self.age = age

    def set_height(self, age: int = 1) -> None:
        self.age = age
    
    def __init__(self, name: str, height: [int | None] = None, age: [int | None] = None) -> None:
        try:
            secure_create(height, age)
        self.name = name
        self.age = age
        self.growth = 0
        print(f"Plant created: {self.name} ({self.height}cm, {self.age} days)")


print("=== Garden Security System ===")

rose: SecurePlant = ["Rose", 10, 10]
rose.get_info()
