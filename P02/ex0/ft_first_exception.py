def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temp > 40:
        print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
        return None
    elif temp < 0:
        print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
        return None
    else:
        print(f"Temperature {temp}ºC is perfect for plants!")
        return temp


def test_temperature_input(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    check_temperature(temp_str)
    print()


print("=== Garden Temperature Checker ===\n")
test_temperature_input("25")
test_temperature_input("abc")
test_temperature_input("100")
test_temperature_input("-50")
print("All tests completed - program didn't crash!")
