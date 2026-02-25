from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import CardError
from typing import Any


def main() -> None:
    game_state: dict[str, Any] = {
        "player": {
            "mana": 15,
            "cards": [],
        },
        "enemy": {
            "mana": 10,
            "cards": [],
        }
    }

    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    try:
        deck.add_card(SpellCard("Lightning Bolt", 4, "common",
                                "damage"))
        deck.add_card(ArtifactCard("Mana Crystal", 3, "Uncommon",
                                   5, "Permanent: +1 mana per turn"))
        deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 10, 5))
    except ValueError as e:
        print(e)

    deck.shuffle()

    print(f"Deck stats: {deck.get_deck_stats()}")

    print()
    print("Drawing and playing cards:\n")
    while len(deck.cards) > 0:
        card_drew = deck.draw_card()
        deck.remove_card(card_drew.name)
        print(f"Drew: {card_drew.name} "
              f"({card_drew.__class__.__name__.removesuffix('Card')})")
        try:
            print(f"Play result: {card_drew.play(game_state)}\n")
        except CardError as e:
            print(e)

    print("Polymorphism in action: Same interface, differnt card behaviors")


if __name__ == "__main__":
    main()
