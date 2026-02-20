from .FantasyCardFactory import FantasyCardFactory
from ex0.CreatureCard import CreatureCard


def main() -> None:
    fantasy = FantasyCardFactory()

    card: CreatureCard = fantasy.create_creature("Fire Dragon")

    print(fantasy.create_themed_deck(60))


if __name__ == "__main__":
    main()
