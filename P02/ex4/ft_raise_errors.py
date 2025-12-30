def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Plant 'tomato' is healthy")


print("=== Garden Plant Health Checker ===\n")
test_plant_checks()
print("\nAll error raising tests completed!")
