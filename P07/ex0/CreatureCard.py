from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, 
                 attack: int, health: int) -> None:
        pass

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass
