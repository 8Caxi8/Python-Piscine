class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int | None = None) -> None:
        try:
            self._height = self.secure_height(height)
            print(f"Height updated: {self._height}cm [OK]")
        except ValueError as e:
            print(e)
    
    def secure_height(self, height: int | None = None) -> int:
        if height is None:
            raise ValueError("Invalid operation attempted: "
                             "height must be provided")
        try:
            height = int(height)
        except (TypeError, ValueError):
            raise ValueError("Invalid operation attempted: "
                             f"height {height}cm [REJECTED]")
        if height < 0:
            raise ValueError("Security: Negative height rejected")
        return height

    def secure_age(self, age: int | None = None) -> int:
        if age is None:
            raise ValueError("Invalid operation attempted: "
                             "age must be provided")
        try:
            age = int(age)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid age {age} days [REJECTED]")
        if age < 0:
            raise ValueError("Security: Negative age rejected")
        return age
    
    def set_age(self, age: int | None = None) -> None:
        try:
            self._age = self.secure_age(age)
            print(f"Age updated: {self._age} days [OK]")
        except ValueError as e:
            print(e)

    def get_info(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height


print("=== Garden Security System ===")

rose: SecurePlant = SecurePlant("Rose", 25, 30)
rose.get_info()
print()
rose.set_height(5.2)
print()
rose.get_info()
