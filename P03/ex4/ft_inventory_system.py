def get_total_items(inventory: dict) -> int:
    no: int = 0
    for value in inventory.values():
        no += value
    return no


def display_inventory(inventory: dict) -> None:
    print("=== Current Inventory ===")
    no: int = get_total_items(inventory)
    for key, value in inventory.items():
        perc: float = value / no * 100
        print(f"{key}: {value} units ({perc:.1f}%)")
    print()


def inventory_stats(inventory: dict) -> None:
    max: int = 0
    min: int = 10
    max_item: str
    min_item: str

    for item, value in inventory.items():
        if value > max:
            max_item = item
            max = value
        if value < min:
            min_item = item
            min = value

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {max_item} ({max} units)")
    print(f"Least abundant: {min_item} ({min} units)\n")


def inventory_categories(inventory: dict) -> None:
    moderate: dict = dict()
    scarce: dict = dict()

    for item, value in inventory.items():
        if value >= 5:
            moderate[item] = value
        else:
            scarce[item] = value

    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")


def management_sugestions(inventory: dict) -> None:
    moderate: list = []

    for item, value in inventory.items():
        if value == 1:
            moderate.append(item)

    print("=== Management Suggestions ===")
    print(f"Restock needed: {moderate}\n")


def dictionary_properties(inventory: dict) -> None:
    keys: list = []
    values: list = []

    for key, value in inventory.items():
        keys.append(key)
        values.append(value)

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")

    key_test: str = "sword"

    print(f"Sample lookup - '{key_test}' in inventory: {key in inventory}\n")


def calculate_score(inventory: dict, catalog: dict) -> None:
    total_score: int = 0

    for key, value in inventory.items():
        total_score += catalog[key]["value"] * value

    print("=== Calculating score ===")
    print(f"Inventory score: {total_score}\n")


def inventory_system() -> None:
    inventory: dict = {
        "potion": 5,
        "chest_armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1,
    }

    catalog: dict = {
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

    display_inventory(inventory)

    inventory_stats(inventory)

    inventory_categories(inventory)

    management_sugestions(inventory)

    dictionary_properties(inventory)

    calculate_score(inventory, catalog)


if __name__ == "__main__":
    inventory_system()
