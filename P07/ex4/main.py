from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5,
                            3, "Melee", "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, "Common", 3, 3,
                            2, "Ranged", "wizard_001")

    print("Registering Tournament Cards...")
    tournament = TournamentPlatform()

    print(tournament.register_card(dragon))
    print()
    print(tournament.register_card(wizard))
    print()

    print("creating tournament match...")
    print(f"Match result: {tournament.create_match(dragon.id, wizard.id)}\n")

    print("Platform Report:")
    print(f"{i}. {tournament.get_leaderboard()}")




if __name__ == "__main__":
    main()
