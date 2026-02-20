from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
import random


class AgressiveStrategy:
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played: list[Card] = [card.name for card in hand if card.cost <= 3]

        return {
            "cards_played": played,
            "mana_used": sum(card.mana for card in played),
            "targets_attacked": self.prioritize_targets(battlefield),
            "damage_dealt": sum(card.attack for card in played
                                if isinstance(card, (CreatureCard, SpellCard)))
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [random.choice(available_targets)]
