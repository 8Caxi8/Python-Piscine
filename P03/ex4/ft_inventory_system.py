def get_total_items(inventory: dict[str, int]) -> int:
    return sum(inventory.values())


def display_inventory(inventory: dict[str, int]) -> None:
    no: int = get_total_items(inventory)

    if no == 0:
        return

    for key, value in inventory.items():
        perc: float = value / no * 100
        print(f"{key}: {value} units ({perc:.1f}%)")
    print()


def inventory_stats(inventory: dict[str, int]) -> None:
    max_item: str = max(inventory, key=inventory.get)
    min_item: str = min(inventory, key=inventory.get)

    print(f"Most abundant: {max_item} ({inventory[max_item]} units)")
    print(f"Least abundant: {min_item} ({inventory[min_item]} units)\n")


def inventory_categories(inventory: dict[str, int]) -> None:
    moderate: dict[str, int] = {
        item: value for item, value in inventory.items()
        if value >= 5
    }
    scarce: dict[str, int] = {
        item: value for item, value in inventory.items()
        if value < 5
    }
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")


def management_suggestions(inventory: dict[str, int]) -> None:
    moderate: list[str] = []

    for item, value in inventory.items():
        if value == 1:
            moderate.append(item)

    print(f"Restock needed: {moderate}\n")


def dictionary_properties(inventory: dict[str, int]) -> None:
    keys: list[str] = list(inventory.keys())
    values: list[int] = list(inventory.values())

    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")

    key_test: str = "sword"

    print(f"Sample lookup - '{key_test}' in inventory: "
          f"{key_test in inventory}\n")


def calculate_score(inventory: dict[str, int],
                    catalog: dict[str, dict[str, str | int]]) -> None:
    total_score: int = 0

    for key, value in inventory.items():
        total_score += catalog[key]["value"] * value

    print(f"Inventory score: {total_score}\n")


def main() -> None:
    inventory: dict[str, int] = {
        "potion": 5,
        "chest_armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1,
    }

    catalog: dict[str, dict[str, str | int]] = {
        "chest_armor": {
            "type": "armor",
            "value": 150,
            "rarity": "uncommon",
        },
        "shield": {
            "type": "weapon",
            "value": 100,
            "rarity": "common",
        },
        "sword": {
            "type": "weapon",
            "value": 250,
            "rarity": "rare",
        },
        "helmet": {
            "type": "armor",
            "value": 350,
            "rarity": "legendary",
        },
        "potion": {
            "type": "consumable",
            "value": 50,
            "rarity": "common",
        },
    }

    print("=== Inventory System Analysis ===")

    no: int = get_total_items(inventory)
    print(f"Total items in inventory: {no}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    display_inventory(inventory)

    print("=== Inventory Statistics ===")
    inventory_stats(inventory)

    print("=== Item Categories ===")
    inventory_categories(inventory)

    print("=== Management Suggestions ===")
    management_suggestions(inventory)

    print("=== Dictionary Properties Demo ===")
    dictionary_properties(inventory)

    print("=== Calculating score ===")
    calculate_score(inventory, catalog)


if __name__ == "__main__":
    main()
