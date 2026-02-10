from alchemy.grimoire import validate_ingredients, record_spell


def ingredient_validation() -> None:
    print("Testing ingredient validation:")

    ingredients = "fire air"
    print(f'validate_ingredients("{ingredients}"): '
          f"{validate_ingredients(ingredients)}")

    ingredients = "dragon scales"
    print(f'validate_ingredients("{ingredients}"): '
          f"{validate_ingredients(ingredients)}\n")


def spell_record() -> None:
    print("Testing spell recording with validation:")

    spell, ingredient = "Fireball", "fire air"
    print(f'record_spell("{spell}", "{ingredient}"): '
          f"{record_spell(spell, ingredient)}")

    spell, ingredient = "Dark Magic", "shadow"
    print(f'record_spell("{spell}", "{ingredient}"): '
          f"{record_spell(spell, ingredient)}\n")


def late_import() -> None:
    print("Testing late import technique:")

    spell, ingredient = "Lightning", "air"
    print(f'record_spell("{spell}", "{ingredient}"): '
          f"{record_spell(spell, ingredient)}\n")


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    ingredient_validation()
    spell_record()
    late_import()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
