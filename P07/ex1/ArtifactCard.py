from ex0.Card import Card
from ex0.Card import CardError


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect

    def play(self, game_state: dict) -> dict:
        if game_state["player"]["mana"] >= self.cost:
            game_state["player"]["mana"] -= self.cost
            game_state["player"]["cards"].append(self)
        else:
            raise CardError("Error: Not enough mana!")

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self._effect
        }

    def activate_ability(self) -> dict:
        print(f"{self.name} activated!")
        return {}
