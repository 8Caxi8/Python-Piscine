from .EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def print_capabilities() -> None:
    capabilities: dict[str, list[str]] = {}

    methods = {
        name
        for name, value in EliteCard.__dict__.items()
        if callable(value) and not name.startswith("_")
    }

    for parent in EliteCard.__mro__[1:]:

        parent_methods = set(parent.__dict__.keys())
        implemented = sorted(methods & parent_methods)

        if implemented:
            capabilities[str(parent.__name__)] = list(implemented)

    for type, type_methods in capabilities.items():
        print(f"- {type}: {type_methods}")
    print()


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print_capabilities()

    print("Playing Arcane Warrior (Elite Card):\n")

    elite = EliteCard("Arcane Warrior", 5, "Legendary",
                      5, 10, 3, "Fireball", 4, 3)

    enemy = CreatureCard("Enemy", 3, "Common", 2, 1)
    enemy1 = CreatureCard("Enemy1", 3, "Common", 2, 1)
    enemy2 = CreatureCard("Enemy2", 3, "Common", 2, 1)

    print("Combat phase:")
    print(f"Attack result: {elite.attack(enemy)}")
    print(f"Defense result: {elite.defend(2)}\n")

    print("Magic Phase:")
    print(f"Spell cast: {elite.cast_spell("Fireball", [enemy1, enemy2])}")
    print(f"Mana channel: {elite.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
