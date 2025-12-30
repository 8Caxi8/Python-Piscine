def test_error_types(error: str) -> None:
    try:
        garden_operations(error)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    except Exception as e:
        print(f"Caught {e}")
    print()


def garden_operations(error: str) -> None:
    print(f"Testing {error}...")
    if error == "ValueError":
        int("abc")
    elif error == "ZeroDivisionError":
        10 / 0
    elif error == "FileNotFoundError":
        with open("missing.txt"):
            pass
    elif error == "KeyError":
        plants = {"rose": 1, "violet": 2}
        print(plants['missing_plant'])
    elif error == "multiple errors together":
        try:
            int("abc")
            10 / 0
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            raise Exception("an error, but program continues!")


print("=== Garden Error Types Demo ===\n")
for err in ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError",
            "multiple errors together"]:
    test_error_types(err)
print("All error types tested successfully!")
