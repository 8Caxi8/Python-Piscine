from ex0.Card import Card
from .Magical import Magical
from .Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target: Card) -> dict:
        pass

    def cast_spell(self, spell_name: str,
                   targets: list[Card]) -> dict:
        pass
