import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def method_1() -> None:
    """
    Method imported directtly from alchemy.elements
    """
    result = alchemy.elements.create_fire()

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): "
          f"{result}\n")


def method_2() -> None:
    """
    Method imported from alchemy.elements import create_water
    """
    result = create_water()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {result}\n")


def method_3() -> None:
    """
    Method imported as a specific name, like heal()
    """
    result = heal()

    print("Method 3 - Aliased import:")
    print(f"heal(): {result}\n")


def method_4() -> None:
    """
    Multiple imports in the same line
    """
    result = strength_potion()

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {result}\n")


def main() -> None:
    print("=== Import Transmutation Mastery ===\n")

    method_1()

    method_2()

    method_3()

    method_4()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
