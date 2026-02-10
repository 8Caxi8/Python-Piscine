import alchemy
from typing import List


def direct_access() -> None:
    names: List[str] = [
        "create_fire", "create_water",
        "create_earth", "create_air"
        ]

    print("Testing direct module access:")
    for element in names:
        try:
            func = getattr(alchemy.elements, element)
            result = func()
            print(f"alchemy.elements.{element}(): {result}")
        except AttributeError as e:
            print(f"alchemy.elements.{element}(): "
                  f"{e.__class__.__name__} - not exposed")


def package_access() -> None:
    names: List[str] = [
        "create_fire", "create_water",
        "create_earth", "create_air"
        ]

    print("Testing package-level access (controlled by __init__.py):")
    for element in names:
        try:
            func = getattr(alchemy, element)
            result = func()
            print(f"alchemy.{element}(): {result}")
        except AttributeError as e:
            print(f"alchemy.{element}(): "
                  f"{e.__class__.__name__} - not exposed")


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")

    direct_access()
    print()
    package_access()
    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
