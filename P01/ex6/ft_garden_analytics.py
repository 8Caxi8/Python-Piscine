class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def __str__(self) -> str:
        return f"- {self.name}: {self._height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self._color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, {self._color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self._prize = prize

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self._prize}"


class Garden:
    def __init__(self, garden_name: str) -> None:
        self._garden_name = garden_name
        self._plants: list[Plant] = []
        self._score = 0

    def add_plant(self, plant: Plant) -> None:
        self._plants.append(plant)
        print(f"Added {plant.name} to {self._garden_name}'s garden")

    def add_score(self, score: int) -> None:
        self._score += score


class GardenManager:
    def __init__(self, garden: Garden) -> None:
        self._garden = garden

    def create_garden_network(self, garden: Garden) -> None:
        pass


class GardenStats(GardenManager):



def create_plants(data_list: list[list[int | str]]) -> list[Plant]:
    plants: list[Plant] = []
    no: int = 0
    for data in data_list:
        plants.append(Plant(*data))
        no += 1
    else:
        print(f"\nTotal plants created: {no}")
        