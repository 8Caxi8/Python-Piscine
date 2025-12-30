def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant in {"tomato", "lettuce", "carrots"}:
                print(f"Watering {plant}")
            else:
                raise Exception(plant)
    except Exception as e:
        print(f"Error: Cannot water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants({"tomato", None})


print("=== Garden Watering System ===\n")
test_watering_system()
print("\n Cleanup always happens, even with errors!")
