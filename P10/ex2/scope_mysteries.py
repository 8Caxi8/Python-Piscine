from typing import Any, Callable


def mage_counter() -> Callable[[], int]:
    i: int = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanting(item: str) -> str:
        return " ".join([enchantment_type, item])

    return enchanting


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> None:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    count = mage_counter()

    print("\nTesting mage counter...")
    for i in range(1, 4):
        print(f"Call {i}: {count()}")

    starting_power = 5
    accumulator = spell_accumulator(starting_power)
    print("\nTesting spell accumulator...")
    print(f"Starting power: {starting_power}")
    for i in range(1, 4):
        print(f"  -Adding 3: {accumulator(3)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))
    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    memory["store"]("sword", flaming("Sword"))
    memory["store"]("shield", frozen("Shield"))
    print(f"Sword: {memory['recall']('sword')}")
    print(f"Shield: {memory['recall']('shield')}")


if __name__ == "__main__":
    main()
