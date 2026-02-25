from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from typing import Any


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._strategy = strategy
        self._factory = factory
        self._cards_created = 0
        self._game_state: dict[str, Any] = {
            "player": {
                "mana": 10,
                "cards": [],
            },
            "enemy": {
                "mana": 10,
                "cards": ["Enemy Player"],
            },
            "actions": [],
            "turns": 0
        }

        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {self._strategy.get_strategy_name()}")
        print("Available types: "
              f"{self._factory.get_supported_types()}\n")

    def simulate_turn(self) -> dict:
        print("Simulating aggressive turn...")

        self._game_state["player"]["cards"].append(
            self._factory.create_creature("Fire Dragon"))
        self._game_state["player"]["cards"].append(
            self._factory.create_creature("Goblin Warrior"))
        self._game_state["player"]["cards"].append(
            self._factory.create_spell("Lightning Bolt"))
        self._cards_created += 3

        hand = [f'{card.name} ({card.cost})'
                for card in self._game_state['player']['cards']]
        print(f"Hand: {hand}\n")

        print("Turn execution:")
        print(f"Strategy: {self._strategy.get_strategy_name()}")

        self._game_state["turns"] += 1
        action = self._strategy.execute_turn(
            self._game_state["player"]["cards"],
            self._game_state["enemy"]["cards"])
        self._game_state["actions"].append(action)
        return action

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._game_state["turns"],
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": sum(action["damage_dealt"]
                                for action in self._game_state["actions"]),
            "cards_created": self._cards_created
        }
