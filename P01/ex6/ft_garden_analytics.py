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


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._color} color"

class PrizeFlower


def create_plants(data_list: list[list[int | str]]) -> list[Plant]:
    plants: list[Plant] = []
    no: int = 0
    for data in data_list:
        plants.append(Plant(*data))
        no += 1
    else:
        print(f"\nTotal plants created: {no}")
        