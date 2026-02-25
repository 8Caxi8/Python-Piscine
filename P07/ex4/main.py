from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
from ex0.Card import CardError


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 3,
                            3, "Melee", "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, "Common", 6, 3,
                            3, "Ranged", "wizard_001")

    print("Registering Tournament Cards...\n")
    tournament = TournamentPlatform()

    print(tournament.register_card(dragon))
    print()
    print(tournament.register_card(wizard))
    print()

    print("Creating tournament match...")
    try:
        print("Match result: "
              f"{tournament.create_match(dragon.id, wizard.id)}\n")
    except CardError as e:
        print(e)

    print("Tournament Leaderboard:")
    for i, card in enumerate(tournament.get_leaderboard(), 1):
        print(f"{i}. {card}")
    print()

    print("Platform Report:")
    try:
        print(tournament.generate_tournament_report())
    except CardError as e:
        print(e)

    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
