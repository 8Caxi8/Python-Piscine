from typing import Callable, Any


def attacks() -> str:
    return "Fireball hits Dragon"


def heals() -> str:
    return "Heals Dragon"


def fireball(mana: int) -> int:
    return 10


def has_mana(mana: int) -> bool:
    if mana <= 5:
        return True

    return False


def spell_combiner(spell1: Callable[[], str], spell2: Callable[[], str]) \
                                                        -> Callable[..., Any]:
    def combined(*args, **kwargs):
        return spell1(*args, **kwargs), spell2(*args, **kwargs)
    return combined


def power_amplifier(base_spell: Callable[[int], int], multiplier: int) \
                                                    -> Callable[..., Any]:
    def amplified(*args, **kwargs):
        return multiplier * base_spell(*args, **kwargs)
    return amplified


def conditional_caster(condition: Callable[[int], bool],
                       spell: Callable[[int], int]) -> Callable[..., Any]:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)

        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
    mana: int = 5

    print("\nTesting spell combiner...")
    combined = spell_combiner(attacks, heals)
    print(f"Combined spell result: {combined()}")
    print("\nTesting power amplifier...")
    amplified = power_amplifier(lambda: fireball(1), 3)
    print(f"Original: {fireball(1)}, Amplified: {amplified()}")
    print("\nTesting conditional caster...")
    cast = conditional_caster(lambda: has_mana(mana), lambda: fireball(mana))
    print(f"Mana required: {mana}/5, result: {cast()}")
    print("\nTesting spell sequence...")
    spells = spell_sequence([attacks, heals])
    print("Spells: ")
    for spell in spells():
        print(f"  - {spell}")


if __name__ == "__main__":
    main()
