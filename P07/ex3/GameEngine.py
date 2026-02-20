from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        

    def get_engine_status(self) -> dict:
        pass
