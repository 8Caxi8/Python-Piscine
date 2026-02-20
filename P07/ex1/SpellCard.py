from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self._effects = ["damage", "heal",  "buff", "debuff"]

        if effect_type not in self._effects:
            raise ValueError("SpellCardError: "
                             "effect '{effect_type}' unknown!")
        match effect_type:
            case "damage":
                self.effect_type = "Deal 3 damage to target"
                self.attack = 3
            case "heal":
                self.effect_type = "Heal 3 health points to target"
                self.attack = 0
            case "buff":
                self.effect_type = "Increase +1 attack to target"
                self.attack = 0
            case "debuff":
                self.effect_type = "Decrease -3 armor to target"
                self.attack = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        print(f"{self.name} resolved!")
        return {}
