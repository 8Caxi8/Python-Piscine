class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int = 1) -> None:
        self.height += growth
        self.growth += growth

    def aged(self, age: int = 1) -> None:
        self.age += age


rose: Plant = Plant("Rose", 25, 30)
sunflower: Plant = Plant("Sunflower", 80, 45)
cactus: Plant = Plant("Cactus", 15, 120)
plants: list[Plant] = [rose, sunflower, cactus]

i: int = 1
while i <= 7:
    print(f" === Day {i} ===")
    for plant in plants:
        plant.get_info()
    if i < 7:
        for plant in plants:
            plant.aged()
        rose.grow(3)
        cactus.grow(-2)
        sunflower.grow()
    i += 1

print("Growth this week:")
print(f"{rose.name}: {rose.growth:+}cm")
print(f"{sunflower.name}: {sunflower.growth:+}cm")
print(f"{cactus.name}: {cactus.growth:+}cm")
