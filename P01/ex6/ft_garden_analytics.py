class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def __str__(self) -> str:
        return f"- {self.name}: {self._height}cm"

    def grow(self) -> None:
        self._height += 1


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
        self._no = 0
        self._growth = 0
        self._types = {"regular": 0,
                       "flowering": 0,
                       "prize flowers": 0
                       }

    def add_plant(self, plant: Plant) -> None:
        self._plants.append(plant)
        self._no += 1
        if isinstance(plant, PrizeFlower):
            self._types["prize flowers"] += 1
        elif isinstance(plant, FloweringPlant):
            self._types["flowering"] += 1
        else:
            self._types["regular"] += 1
        print(f"Added {plant.name} to {self._garden_name}'s garden")

    def add_score(self, score: int) -> None:
        self._score += score

    def grow_plants(self) -> None:
        print(f"{self._garden_name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()
            self._growth += 1
            self._score += 25
            print(f"{plant.name} grew 1cm")
        print("")


class GardenManager:
    def __init__(self) -> None:
        self._gardens: list[Garden] = []

    def create_garden_network(self, plants: list[Plant],
                              garden: Garden) -> None:
        for plant in plants:
            garden.add_plant(plant)
        print("")
        self._gardens.append(garden)

    def garden_report(self, garden: Garden) -> None:
        self._stats = GardenStats(garden)
        self._stats.report_stats()
        score_strings = [f"{garden._garden_name}: {garden._score}"
                         for garden in self._gardens]
        print("Garden scores - " + ", ".join(score_strings))
        print(f"Total gardens managed: {len(score_strings)}")
        print("")


class GardenStats:
    def __init__(self, garden: Garden) -> None:
        self._garden = garden

    def report_stats(self) -> None:
        print(f"=== {self._garden._garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self._garden._plants:
            print(plant)
        print(f"\nPlants added: {self._garden._no}, "
              f"Total growth: {self._garden._growth}")
        print(f"Plant types: "
              f"{self._garden._types['regular']} regular, "
              f"{self._garden._types['flowering']} flowering, "
              f"{self._garden._types['prize flowers']} prize flowers")
        print("")


def create_plants(data_list: list[list[int | str]]) -> list[Plant]:
    plants: list[Plant] = []
    no: int = 0
    for data in data_list:
        plants.append(Plant(*data))
        no += 1
    else:
        print(f"\nTotal plants created: {no}")
    return plants


print("=== Garden Management System Demo ===\n")

sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)
rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
oak: Plant = Plant("Oak Tree", 100)
tulip: FloweringPlant = FloweringPlant("Tulip", 30, "Violet")

aliceplants = [oak, rose, sunflower]
bobplants = [tulip]

alice: Garden = Garden("Alice")
bob: Garden = Garden("Bob")
manager: GardenManager = GardenManager()

manager.create_garden_network(aliceplants, alice)
manager.create_garden_network(bobplants, bob)
alice.grow_plants()

manager.garden_report(alice)
manager.garden_report(bob)
