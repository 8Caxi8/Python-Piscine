from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard info:")
    print(fire_dragon.get_card_info())
    print()

    print("Playing Fire Dragon with 6 mana available:")
    print(f"playable: {fire_dragon.is_playable(10)}")
    print(f"Play result: {fire_dragon.play({})}")
    print()

    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Commun", 2, 3)
    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"playable: {fire_dragon.is_playable(3)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
