from ex0.Card import Card
from .Magical import Magical
from .Combatable import Combatable


class SpellError(Exception):
    pass


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, armor: int,
                 spell_name: str, spell_cost: int, spell_damage: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Elite"
        self._attack = attack
        self._armor = armor
        self._health = health
        self.spell_name = spell_name
        self.spell_cost = spell_cost
        self._spell_damage = spell_damage
        self._combat_type = "melee"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite summoned to battlefield"
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self._attack,
            "health": self._health,
            "spell": self.spell_name,
            "spell_cost": self.spell_cost,
            "spell_damage": self._spell_damage
        })
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self._attack,
            "combat_type": self._combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self._armor,
            "still_alive": self._health > incoming_damage - self._armor
        }

    def get_combat_stats(self) -> dict:
        return {
            "card_name": self.name,
            "attack_damage": self._attack,
            "physical_armor": self._armor,
            "combat_type": self._combat_type
        }

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        if spell_name != self.spell_name:
            raise SpellError("Trying wrong spell!")

        return {
            "caster": self.name,
            "spell": self.spell_name,
            "targets": [enemy.name for enemy in targets],
            "mana_used": self.spell_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": self.spell_cost + amount
        }

    def get_magic_stats(self) -> dict:
        return {
            "card_name": self.name,
            "spell": self.spell_name,
            "spell_damage": self._spell_damage,
            "spell_cost": self.spell_cost,
        }
