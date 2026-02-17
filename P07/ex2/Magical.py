from abc import ABC
from ex0.Card import Card


class Magical(ABC):
    def cast_spell(self, spell_name: str,
                   targets: list[Card]) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
