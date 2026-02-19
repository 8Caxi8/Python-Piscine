from .FantasyCardFactory import FantasyCardFactory


def main() -> None:
    fantasy = FantasyCardFactory()

    card = fantasy.create_creature()


if __name__ == "__main__":
    main()
