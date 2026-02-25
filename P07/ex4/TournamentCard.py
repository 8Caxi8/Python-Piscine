from ex0.Card import Card
from ex0.Card import CardError
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, armor: int,
                 combat_type: str, id: str) -> None:
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._armor = armor
        self._base_health = health
        self._health = health
        self._combat_type = combat_type
        self.wins = 0
        self.losses = 0
        self.id = id

    def play(self, game_state: dict) -> dict:
        if game_state["player"]["mana"] >= self.cost:
            game_state["player"]["mana"] -= self.cost
            game_state["player"]["cards"].append(self)
        else:
            raise CardError("Error: Not enough mana!")

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament Card summoned to battlefield"
        }

    def attack(self, target: Card) -> dict:
        if isinstance(target, TournamentCard):
            still_alive = target.defend(self._attack)["still_alive"]
        else:
            still_alive = False

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self._attack,
            "combat_type": self._combat_type,
            "still_alive": still_alive
            }

    def defend(self, incoming_damage: int) -> dict:
        result = incoming_damage - self._armor

        if result > 0:
            self._health -= result

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self._armor,
            "still_alive": self._health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "card_name": self.name,
            "attack_damage": self._attack,
            "physical_armor": self._armor,
            "combat_type": self._combat_type
        }

    def calculate_rating(self) -> int:
        base_rank = (int(self._attack * 50 + self._armor *
                     140 + self._base_health * 143.5))

        return (base_rank + 16 * (self.wins - self.losses))

    def update_wins(self, wins: int) -> None:
        i_wins = int(wins)
        if i_wins < 0:
            raise ValueError(f"Error: {wins} must be positive!")

        self.wins = i_wins

    def update_losses(self, losses: int) -> None:
        i_losses = int(losses)
        if i_losses < 0:
            raise ValueError(f"Error: {losses} must be positive!")

        self.losses = i_losses

    def get_rank_info(self) -> dict:
        return {
            "Rating": self.calculate_rating(),
            "Record": f"{self.wins}-{self.losses}"
        }
