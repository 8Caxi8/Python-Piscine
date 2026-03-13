import functools
import operator
from typing import Callable, Any


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


def partial_enchanter(base_enchantment: Callable[..., Any]) \
                                            -> dict[str, Callable[..., Any]]:
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., Any]:
    @functools.singledispatch
    def spell(value):
        raise TypeError("Unsupported spell type")

    @spell.register
    def _(value: int) -> str:
        return f"Spell deal {value} damage."

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment applied: {value}"

    @spell.register
    def _(value: list) -> list[str]:
        return [spell(v) for v in value]

    return spell


def base_enchantment(power: int, element: str, target: str) \
                                                -> dict[str, int | str]:
    return {
        "power": power,
        "element": element,
        "target": target,
        }


def main() -> None:
    try:
        print("\nTesting spell reducer...")
        spells = [i for i in range(1, 40)]
        print(f"Sum: {spell_reducer(spells, 'add')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")
    except ValueError as e:
        print(e)

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(f"  - Fire: {enchant['fire_enchant']('sword')}")
    print(f"  - Ice: {enchant['ice_enchant']('shield')}")
    print(f"  - Lightning: {enchant['lightning_enchant']('helmet')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    try:
        print("\nTesting spell dispather...")
        dispatch = spell_dispatcher()
        print(f"Spell: {dispatch(10)}")
        print(f"Enchant: {dispatch('Mana channeling')}")
        print(f"Multicast: {dispatch([5, 3, 'Cooldown reduction'])}")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
