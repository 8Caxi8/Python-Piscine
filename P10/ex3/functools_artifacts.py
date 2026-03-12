import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case "add":
            return functools.reduce(operator.add, spells)
        case "multiply":
            return functools.reduce(operator.mul, spells)
        case "max":
            return functools.reduce(max, spells)
        case "min":
            return functools.reduce(min, spells)
        case _:
            raise ValueError("[Error]: Invalid Operation")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache
def memorized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    pass


def base_enchantment(power: int, element: str, target: str) \
                                                -> dict[str, int | str]:
    return {
        "power": power,
        "element": element,
        "target": target,
        }


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [i for i in range(1, 40)]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(f"  - Fire: {enchant['fire_enchant']('sword')}")
    print(f"  - Ice: {enchant['ice_enchant']('shield')}")
    print(f"  - Lightning: {enchant['lightning_enchant']('helmet')}")

    print("\nTesting memorized fibonacci...")
    print(f"Fib(10): {memorized_fibonacci(10)}")
    print(f"Fib(15): {memorized_fibonacci(15)}")

    print("\nTesting spell dispather...")


if __name__ == "__main__":
    main()
