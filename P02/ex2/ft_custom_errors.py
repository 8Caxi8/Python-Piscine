class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __str__(self) -> str:
        return "The tomato plant is wilting!"


class WaterError(GardenError):
    def __str__(self) -> str:
        return "Not enough water in the tank!"


def check_plant_health(age: int) -> None:
    if age > 30:
        raise PlantError()


def check_water_plants(tank: int) -> None:
    if tank <= 0:
        raise WaterError()


def catching_errors(age: int, tank: int) -> None:
    try:
        check_plant_health(age)
        check_water_plants(tank)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def catching_garden_errors(age: int, tank: int) -> None:
    try:
        check_plant_health(age)
        check_water_plants(tank)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


print("=== Custom Garden Errors Demo ===\n")

print("Testing PlantError...")
catching_errors(40, 20)
print("\nTesting WaterError...")
catching_errors(10, -5)

print("\nTesting catching all garden errors...")
catching_garden_errors(40, 20)
catching_garden_errors(10, -5)
print("\nAll custom error types work correctly")
