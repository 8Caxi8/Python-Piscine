class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int = 1) -> None:
        self.height += growth
        self.growth += growth

    def aged(self, age: int = 1) -> None:
        self.age += age


def create_plants(data_list: list[list[int | str]]) -> list[Plant]:
    plants: list[Plant] = []
    no: int = 0
    for data in data_list:
        plants.append(Plant(*data))
        no += 1
    else:
        print(f"\nTotal plants created: {no}")


plant_data: list[list[int | str]] = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]]
print("=== Plant Factory Output ===")
plants: list[Plant] = create_plants(plant_data)
