from .EliteCard import EliteCard
from ex0.Card import CardError
from typing import Any


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
    game_state: dict[str, Any] = {
        "player": {
            "mana": 9,
            "cards": [],
        },
        "enemy": {
            "mana": 10,
            "cards": [],
        }
    }

    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print_capabilities()

    print("Playing Arcane Warrior (Elite Card):\n")

    elite = EliteCard("Arcane Warrior", 5, "Legendary",
                      5, 10, 3, "Fireball", 4, 3)

    try:
        elite.play(game_state)
    except CardError as e:
        print(e)

    game_state["enemy"]["cards"].append(
        EliteCard("Enemy", 3, "Common", 2, 1, 1, "Spell1", 2, 2))
    game_state["enemy"]["cards"].append(
        EliteCard("Enemy1", 3, "Common", 2, 1, 1, "Spell1", 2, 2))
    game_state["enemy"]["cards"].append(
        EliteCard("Enemy2", 3, "Common", 2, 1, 1, "Spell1", 2, 2))

    print("Combat phase:")

    target: EliteCard = game_state["enemy"]["cards"][0]
    attack_result = elite.attack(target)
    target_defense = target.defend(attack_result["damage"])
    defense_result = elite.defend(2)

    print(f"Attack result: {attack_result}")
    print(f"Defense result: {defense_result}\n")

    if not target_defense["still_alive"]:
        game_state["enemy"]["cards"].remove(target)
    if not defense_result["still_alive"]:
        game_state["player"]["cards"].remove(elite)

    print("Magic Phase:")
    print("Spell cast: "
          f"{elite.cast_spell('Fireball', game_state['enemy']['cards'])}")

    mana_channeled = elite.channel_mana(3)
    game_state["player"]["mana"] += mana_channeled["channeled"]
    mana_channeled.update({"total_mana": game_state["player"]["mana"]})

    print(f"Mana channel: {mana_channeled}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
