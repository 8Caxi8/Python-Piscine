from .Card import Card


class CardError(Exception):
    pass


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        try:
            self.validate_attack(attack)
            self.validate_health(health)
        except CardError as e:
            raise e

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self._attack,
            "Combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self._attack,
            "health": self._health
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
            self._attack = attack

    def validate_health(self, health: int) -> int:
        try:
            int(health)
            if health <= 0:
                raise ValueError
        except ValueError:
            raise CardError(f"Error creating {self.name}: health value "
                            f"({health}) must be a positive integer!")
        else:
            self._health = health
