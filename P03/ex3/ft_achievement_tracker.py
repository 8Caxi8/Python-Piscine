class Achievements:
    _all_unique: set[str] = {"first_kill", "boss_slayer", "collector",
                             "level_10", "perfectionist", "speed_demon",
                             "treasure_hunter"}

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._achievements: set[str] = set()

    def set_achievement(self, achievements: set[str]) -> None:
        for achievement in achievements:
            if achievement in Achievements._all_unique:
                self._achievements.add(achievement)

    def get_achievements(self) -> set[str]:
        return self._achievements

    def get_missing_achievements(self) -> set[str]:
        return Achievements._all_unique - self._achievements

    @classmethod
    def get_unique(cls) -> set[str]:
        return cls._all_unique


def find_common(players: list[Achievements]) -> set:
    common: set[str] = players[0].get_achievements().copy()

    for player in players[1:]:
        common &= player.get_achievements()

    return common


def find_rare(players: list[Achievements]) -> set[str]:
    all_achievements: set[str] = set()
    duplicates: set[str] = set()

    for player in players:
        ach = player.get_achievements()
        duplicates |= all_achievements & ach
        all_achievements |= ach

    rare = all_achievements - duplicates
    return rare


def achievement_analytics(players: list[Achievements]) -> None:
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {Achievements.get_unique()}")
    print(f"Total unique achievements: {len(Achievements.get_unique())}\n")

    common: set[str] = find_common(players)
    print(f"Common to all players: {common}")

    rare: set[str] = find_rare(players)
    print(f"Rare achievements (1 player): {rare}\n")


def who_is_missing(players: list[Achievements]) -> None:
    for player in players:
        print(f"{player.name} is missing: "
              f"{player.get_missing_achievements()}")
    print()


def create_groups(player1: Achievements, player2: Achievements) -> None:
    common: set[str] = player1.get_achievements().intersection(
        player2.get_achievements())
    P1_unique: set[str] = (player1.get_achievements()
                           - player2.get_achievements())
    P2_unique: set[str] = (player2.get_achievements()
                           - player1.get_achievements())

    print(f"{player1.name} vs {player2.name} common: {common}")
    print(f"{player1.name} unique: {P1_unique}")
    print(f"{player2.name} unique: {P2_unique}\n")


def create_achievements() -> list[Achievements]:
    achiev: list[Achievements] = []
    players: dict[str, set[str]] = {
        "Alice": {
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
        },
        "Bob": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
        },
        "Charlie": {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        }
    }

    for player in players.keys():
        achiev.append(Achievements(player))

    for each, achievements in zip(achiev, players.values()):
        each.set_achievement(achievements)

    return achiev


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achiev: list[Achievements] = create_achievements()
    for each in achiev:
        print(f"Player {each.name} achievements: "
              f"{each.get_achievements()}")
    print()

    achievement_analytics(achiev)

    who_is_missing(achiev)

    create_groups(achiev[0], achiev[1])


if __name__ == "__main__":
    main()
