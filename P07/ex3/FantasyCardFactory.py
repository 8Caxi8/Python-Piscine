from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        self._creatures = [
            ["Fire Dragon", 5, "Legendary", 7, 5],
            ["Goblin Warrior", 2, "Common", 2, 1],
            ["Ice Wizard", 4, "Rare", 3, 4],
            ["Lightning Elemental", 3, "Uncommon", 4, 2],
            ["Stone Golem", 6, "Rare", 5, 8],
            ["Shadow Assassin", 3, "Uncommon", 5, 2],
            ["Healing Angel", 4, "Rare", 2, 6],
            ["Forest Sprite", 1, "Common", 1, 1],
        ]
        return CreatureCard(*random.choice(self._creatures))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass
