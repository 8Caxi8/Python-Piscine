import alchemy
import alchemy.transmutation as tr


def absolute_imports() -> None:
    """
    In basic.py absolute imports are used 'from alchemy.elements'
    """
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {tr.lead_to_gold()}")
    print(f"stone_to_gem(): {tr.stone_to_gem()}\n")


def relative_imports() -> None:
    """
    In advanced.py relative imports are used '..potions'
    """
    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {tr.philosophers_stone()}")
    print(f"elixir_of_life(): {tr.elixir_of_life()}\n")


def package_access() -> None:
    """
    import alchemy gives access tospecifi imports that are available
    in the __init__.py files
    """
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}\n")


def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")

    absolute_imports()

    relative_imports()

    package_access()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
