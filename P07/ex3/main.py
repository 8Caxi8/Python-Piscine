from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AgressiveStrategy
from .GameEngine import GameEngine


def main() -> None:
    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()

    engine = GameEngine()

    print("\n=== DataDeck Game Engine ===\n")

    engine.configure_engine(factory, strategy)
    print(f"Actions: {engine.simulate_turn()}\n")

    print("Game Report:")
    print(f"{engine.get_engine_status()}\n")

    print("Abstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
