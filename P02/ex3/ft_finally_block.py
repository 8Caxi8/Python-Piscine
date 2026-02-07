def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant not in {"tomato", "lettuce", "carrots"}:
                raise ValueError(f"{plant}")

            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system(plant_list: list[str]) -> None:
    try:
        water_plants(plant_list)
        print("Watering completed successfully!\n")

    except ValueError as e:
        print(f"Error: Cannot water {e} - invalid plant!")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    test_watering_system(["tomato", "lettuce", "carrots"])

    print("Testing with error...")
    test_watering_system(["tomato", None])


if __name__ == "__main__":
    main()
