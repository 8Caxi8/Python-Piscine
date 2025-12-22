class Plant:
    name: str
    height: int

    #def __init__(self, name: str, height: int, age: int) -> None:
    #    self.name = name
    #    self.height = height
    #    self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

rose.name 

rose: Plant = Plant("Rose", 25, 30)
sunflower: Plant = Plant("Sunflower", 80, 45)
cactus: Plant = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
rose.print_info()
sunflower.print_info()
cactus.print_info()
