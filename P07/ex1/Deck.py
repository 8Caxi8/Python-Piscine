from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == "card_name":
                self.cards.remove(card)
                return True

        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        deck_stats: dict[str, int | float] = {}
        total_cost: int = 0

        deck_stats.update({"total_cards": len(self.cards)})
        for card in self.cards:
            if isinstance(card, CreatureCard):
                if "creatures" in deck_stats.keys():
                    no = deck_stats["creatures"] + 1
                else:
                    no = 1
                deck_stats.update({"creatures": no})
            elif isinstance(card, ArtifactCard):
                if "artifacts" in deck_stats.keys():
                    no = deck_stats["artifacts"] + 1
                else:
                    no = 1
                deck_stats.update({"artifacts": no})
            elif isinstance(card, SpellCard):
                if "spells" in deck_stats.keys():
                    no = deck_stats["spells"] + 1
                else:
                    no = 1
                deck_stats.update({"spells": no})
            total_cost += card.cost
        deck_stats.update({"avg_cost": total_cost / len(self.cards)})

        return deck_stats
