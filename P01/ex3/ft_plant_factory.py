class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def create_plants(data_list: list[list[int | str]]) -> None:
    plants: list[Plant] = []
    no: int = 0

    for data in data_list:
        plants.append(Plant(*data))
        no += 1
    else:
        print(f"\nTotal plants created: {no}")


def main() -> None:
    plant_data: list[list[int | str]] = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]]

    print("=== Plant Factory Output ===")
    create_plants(plant_data)


if __name__ == "__main__":
    main()
