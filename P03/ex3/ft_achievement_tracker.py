class Achievements():
    _all_unique: set[str] = {"first_kill", "boss_slayer", "collector",
                             "first_kill", "level_10", "perfectionist",
                             "speed_demon", "treasure_hunter"}

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._achievements: set[str] = set()

    def give_achievement(self, achievement: str) -> None:
        if achievement in Achievements._all_unique:
            self._achievements.add(achievement)
        else:
            return

    def list_achievements(self) -> set[str]:
        return self._achievements

    def list_missing_achievements(self) -> set[str]:
        return Achievements._all_unique - self._achievements


def find_common(players: list[Achievements]) -> set:
    common: set = set()
    common = players[0].list_achievements().copy()

    for player in players[1:]:
        common &= player.list_achievements()

    return common


def find_rare(players: list[Achievements]) -> set[str]:
    all_achievements: set[str] = set()
    duplicates: set[str] = set()

    for player in players:
        ach = player.list_achievements()
        duplicates |= all_achievements & ach
        all_achievements |= ach

    rare = all_achievements - duplicates
    return rare


def achivement_analytics(players: list[Achievements]) -> None:
    print("=== Achivement Analytics ===")
    print(f"All unique achivements: {Achievements._all_unique}")
    print(f"Total unique achievements: {len(Achievements._all_unique)}\n")

    common: set = find_common(players)
    print(f"Common to all players: {common}")

    rare: set = find_rare(players)
    print(f"Rare achievements (1 player): {rare}\n")


def who_is_missing(players: list[Achievements]) -> None:
    for player in players:
        print(f"{player.name} is missing: "
              f"{player.list_missing_achievements()}")
    print()


def create_groups(player1: Achievements, player2: Achievements) -> None:
    common: set = player1._achievements.intersection(player2._achievements)
    P1_unique: set = player1._achievements - player2._achievements
    P2_unique: set = player2._achievements - player1._achievements

    print(f"{player1.name} vs {player2.name} common: {common}")
    print(f"{player1.name} unique: {P1_unique}")
    print(f"{player2.name} unique: {P2_unique}\n")


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = Achievements("Alice")
    bob = Achievements("Bob")
    charlie = Achievements("Charlie")

    alice.give_achievement('first_kill')
    alice.give_achievement('level_10')
    alice.give_achievement('treasure_hunter')
    alice.give_achievement('speed_demon')

    bob.give_achievement('first_kill')
    bob.give_achievement('level_10')
    bob.give_achievement('boss_slayer')
    bob.give_achievement('collector')

    charlie.give_achievement('level_10')
    charlie.give_achievement('treasure_hunter')
    charlie.give_achievement('boss_slayer')
    charlie.give_achievement('speed_demon')
    charlie.give_achievement('perfectionist')

    print(f"Player {alice.name} achievements: {alice._achievements}")
    print(f"Player {bob.name} achievements: {bob._achievements}")
    print(f"Player {charlie.name} achievements: {charlie._achievements}\n")

    achivement_analytics([alice, bob, charlie])

    who_is_missing([alice, bob, charlie])

    create_groups(alice, bob)


if __name__ == "__main__":
    achievement_tracker()
