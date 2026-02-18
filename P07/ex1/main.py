from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 4, "common",
                            "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 3, "Uncommon",
                               5, "Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 10, 5))

    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()
    print("Drawing and playing cards:\n")
    while len(deck.cards) > 0:
        card_drew = deck.draw_card()
        deck.remove_card(card_drew.name)
        print(f"Drew: {card_drew.name} "
              f"({card_drew.__class__.__name__.removesuffix('Card')})")
        print(f"Play result: {card_drew.play({})}\n")

    print("Polymorphism in action: Same interface, differnt card behaviors")


if __name__ == "__main__":
    main()
