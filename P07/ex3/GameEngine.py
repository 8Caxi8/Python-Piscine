from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._strategy = strategy
        self._factory = factory
        self._battlefield = ["Enemy Player"]
        self._turns = 0
        self._actions: list = []
        self._cards_created = 0

        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {self._strategy.get_strategy_name()}")
        print("Available types: "
              f"{self._factory.get_supported_types()}\n")

    def simulate_turn(self) -> dict:
        print("Simulating aggressive turn...")

        hand: list[Card] = []
        hand.append(self._factory.create_creature("Fire Dragon"))
        hand.append(self._factory.create_creature("Goblin Warrior"))
        hand.append(self._factory.create_spell("Lightning Bolt"))
        self._cards_created += 3

        print(f"Hand: {[f"{card.name} ({card.cost})" for card in hand]}\n")

        print("Turn execution:")
        print(f"Strategy: {self._strategy.get_strategy_name()}")

        self._turns += 1
        action = self._strategy.execute_turn(hand, self._battlefield)
        self._actions.append(action)
        return action

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns,
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": sum(action["damage_dealt"]
                                for action in self._actions),
            "cards_created": self._cards_created
        }
