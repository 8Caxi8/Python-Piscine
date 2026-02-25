from .Card import Card
from .Card import CardError


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.effect = "Creature summoned to battlefield"
        try:
            self.attack = self.validate_attack(attack)
            self.health = self.validate_health(health)
        except CardError as e:
            raise e

    def play(self, game_state: dict) -> dict:
        if game_state["player"]["mana"] >= self.cost:
            game_state["player"]["mana"] -= self.cost
            game_state["player"]["cards"].append(self)
        else:
            raise CardError("Error: Not enough mana!")

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def attack_target(self, target: Card) -> dict:
        if isinstance(target, CreatureCard):
            combat_resolved = target.health <= self.attack
        else:
            combat_resolved = True

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info

    def validate_attack(self, attack: int) -> int:
        try:
            int(attack)
            if attack <= 0:
                raise ValueError
        except ValueError:
            raise CardError(f"Error creating {self.name}: attack value "
                            f"({attack}) must be a positive integer!")
        else:
            return attack

    def validate_health(self, health: int) -> int:
        try:
            int(health)
            if health <= 0:
                raise ValueError
        except ValueError:
            raise CardError(f"Error creating {self.name}: health value "
                            f"({health}) must be a positive integer!")
        else:
            return health
