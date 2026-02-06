class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

    def __str__(self) -> str:
        return f"- {self.name}: {self._height}cm"

    def grow(self) -> None:
        self._height += 1

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


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
    _garden_count: int = 0

    def __init__(self, garden_name: str) -> None:
        self._garden_name = garden_name
        self._plants: list[Plant] = []
        self._score = 92
        self._no = 0
        self._growth = 0
        self._types = {
            "regular": 0,
            "flowering": 0,
            "prize flowers": 0
        }
        type(self)._garden_count += 1

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
        self.add_score(126)

        for plant in self._plants:
            plant.grow()
            self._growth += 1
            self._score += 25
            print(f"{plant.name} grew 1cm")

        print("")

    @classmethod
    def get_garden_count(cls) -> int:
        return cls._garden_count

    def get_plants(self) -> list[Plant]:
        return self._plants

    def get_growth(self) -> int:
        return self._growth

    def get_plant_type(self, type: str) -> int:
        return self._types[type]

    def get_name(self) -> str:
        return self._garden_name

    def get_no(self) -> int:
        return self._no

    def get_score(self) -> int:
        return self._score


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
        score_strings: list[str] = []
        self.GardenStats(garden).report_stats()

        for garden in self._gardens:
            score_strings.append(f"{garden.get_name()}: {garden.get_score()}")

        print(f"Height validation test: {Plant.validate_height(5)}")
        print("Garden scores - " + ", ".join(score_strings))
        print(f"Total gardens managed: {Garden.get_garden_count()}")
        print("")

    class GardenStats:
        def __init__(self, garden: Garden) -> None:
            self._garden = garden

        def report_stats(self) -> None:
            print(f"=== {self._garden.get_name()}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self._garden.get_plants():
                print(plant)
            print(f"\nPlants added: {self._garden.get_no()}, "
                  f"Total growth: {self._garden.get_growth()}")
            print(f"Plant types: "
                  f"{self._garden.get_plant_type('regular')} regular, "
                  f"{self._garden.get_plant_type('flowering')} flowering, "
                  f"{self._garden.get_plant_type('prize flowers')} "
                  "prize flowers")
            print("")


def main() -> None:
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


if __name__ == "__main__":
    main()
