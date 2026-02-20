from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures: dict[str, list[str | int]] = {
            "Fire Dragon": [5, "Legendary", 7, 5],
            "Goblin Warrior": [2, "Common", 2, 1],
            "Ice Wizard": [4, "Rare", 3, 4],
            "Lightning Elemental": [3, "Uncommon", 4, 2],
            "Stone Golem": [6, "Rare", 5, 8],
            "Shadow Assassin": [3, "Uncommon", 5, 2],
            "Healing Angel": [4, "Rare", 2, 6],
            "Forest Sprite": [1, "Common", 1, 1],
        }
        self._spells: dict[str, list[str | int]] = {
            "Lightning Bolt": [3, "Common", "damage"],
            "Healing Potion": [2, "Common", "heal"],
            "Fireball": [4, "Uncommon", "damage"],
            "Shield Spell": [1, "Common", "buff"],
            "Meteor": [8, "Legendary", "damage"],
            "Ice Shard": [2, "Common", "damage"],
            "Divine Light": [5, "Rare", "heal"],
            "Magic Missile": [1, "Common", "damage"],
        }
        self._artifact: dict[str, list[str | int]] = {
            "Mana Crystal": [2, "Common", 5, "+1 mana per turn"],
            "Sword of Power": [3, "Uncommon", 3,
                               "+2 attack to equipped creature"],
            "Ring of Wisdom": [4, "Rare", 4, "Draw an extra card each turn"],
            "Shield of Defense": [5, "Rare", 6,
                                  "+3 health to all friendly creatures"],
            "Crown of Kings": [7, "Legendary", 8,
                               "+1 cost reduction to all cards"],
            "Boots of Speed": [2, "Uncommon", 2, "Cards cost 1 less mana"],
            "Cloak of Shadows": [3, "Uncommon", 3, "Creatures have stealth"],
            "Staff of Elements": [6, "Legendary", 7, "+1 spell damage"],
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(list(self._creatures.keys()))

            return CreatureCard(name_or_power,
                                *self._creatures[str(name_or_power)])

        elif name_or_power not in self._creatures.keys():
            raise ValueError("Error: Creature {name_or_power] doesn't exist!")

        return CreatureCard(name_or_power,
                            *self._creatures[str(name_or_power)])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(list(self._spells.keys()))

            return SpellCard(name_or_power,
                             *self._spells[str(name_or_power)])

        if name_or_power not in self._spells.keys():
            raise ValueError("Error: Spell {name_or_power] doesn't exist!")

        return SpellCard(name_or_power,
                         *self._spells[str(name_or_power)])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(list(self._artifact.keys()))

            return ArtifactCard(name_or_power,
                                *self._artifact[str(name_or_power)])

        if name_or_power not in self._artifact.keys():
            raise ValueError("Error: Artifact {name_or_power] doesn't exist!")

        return ArtifactCard(name_or_power,
                            *self._artifact[str(name_or_power)])

    def create_themed_deck(self, size: int) -> dict:
        cards: dict[str, list[str | int]] = (
            self._creatures | self._artifact | self._spells)
        if size > len(cards):
            size = len(cards)

        selected_keys = random.sample(list(cards.keys()), size)

        return {"creatures": [key for key in selected_keys
                              if key in self._creatures.keys()],
                "spells": [key for key in selected_keys
                           if key in self._spells.keys()],
                "artifacts": [key for key in selected_keys
                              if key in self._artifact.keys()]}

    def get_supported_types(self) -> dict:
        return {
            "creatures": [creature for creature in self._creatures.keys()],
            "spells": [spell for spell in self._spells.keys()],
            "artifacts": [artifact for artifact in self._artifact.keys()]
        }
