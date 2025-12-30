class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self.height = height
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        try:
            new_age = int(new_age)
        except (TypeError, ValueError):
            print(f"Security: Invalid age {new_age} [REJECTED]")
            return
        if new_age < 0:
            print(f"Security: Negative age {new_age} [REJECTED]")
        else:
            self._age = new_age

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        try:
            new_height = int(new_height)
        except (TypeError, ValueError):
            print(f"Security: Invalid height {new_height} [REJECTED]")
            return
        if new_height < 0:
            print(f"Security: Negative height {new_height} [REJECTED]")
        else:
            self._height = new_height

    def __str__(self) -> str:
        return f"{self._name} ({type(self).__name__}): " \
                f"{self._height}cm, {self._age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self._name} provides 78 square meters of shade")

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 nutritional_value: str, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._harvest_season} harvest\n" \
            f"{self._name} is rich in {self._nutritional_value}"


print("=== Garden Plant Types ===")

rose = Flower("Rose", 25, 30, "red")
violet = Flower("Violet", 25, 30, "violet")

oak = Tree("Oak", 500, 1825, 50)
maple = Tree("Maple", 450, 1041, 35)

tomato = Vegetable("Tomato", 80, 90, "vitamin C", "summer")
lettuce = Vegetable("Lettuce", 20, 100, "vitamin K", "spring")

print(rose)
print(violet)
violet.bloom()
print()
print(oak)
print(maple)
maple.produce_shade()
print()
print(tomato)
print(lettuce)
