import alchemy
from typing import List


def direct_access() -> None:
    """
    Test direct access to element functions
    via the internal alchemy.elements module.

    This function
    attempts to dynamically retrieve and execute a set on predefined
    element-creation funtions from alchemy.elements.
    If it does not exist an AttributeError is raised and caught.
    """

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
    """
    Test package access to each element function.

    This function tries to retrieve and execute element-creation
    functions directly from the alchemy package namespace. Acess depends
    on what is explicitly exposed in the package's __init__.py
    """

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
