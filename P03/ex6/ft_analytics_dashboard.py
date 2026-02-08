from typing import Any


def list_comprehensions(data: dict[str, Any]) -> None:
    high_scores: list[int] = []
    high_scorers: list[str] = []
    active_players: list[str] = []

    high_scorers: list[str] = [
        player
        for player, value in data["players"].items()
        if value["total_score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    high_scores = [
        value["total_score"]
        for value in data["players"].values()
        if value["total_score"] > 2000]
    print(f"High scores: {high_scores}")

    active_players = [
        info["player"]
        for info in data["sessions"]
        if info["duration_minutes"] > 100]
    print(f"Last active players: {active_players}\n")


def dict_comprehensions(data: dict[str, Any]) -> None:
    player_scores: dict[str, int] = {}
    categories: dict[str, str] = {}
    count_scores: dict[str, str] = {}

    player_scores = {
        player: info["total_score"]
        for player, info in data["players"].items()
    }
    print(f"Player scores: {player_scores}")

    categories = {
        mode: {
            player
            for player, info in data["players"].items()
            if info["favorite_mode"] == mode
        }
        for mode in {
            type["favorite_mode"]
            for type in data["players"].values()
        }
    }
    print(f"Player favorite categories: {categories}")

    count_scores = {
        "high": len({
            player
            for player, info in data["players"].items()
            if info["total_score"] > 4000
        }),
        "medium": len({
            player
            for player, info in data["players"].items()
            if 1500 < info["total_score"] <= 4000
        }),
        "low": len({
            player
            for player, info in data["players"].items()
            if info["total_score"] <= 1500
        })
    }
    print(f"Score categories: {count_scores}\n")


def set_comprehensions(data: dict[str, Any]) -> None:
    players: set[str] = set()
    achievements: set[str] = set()
    favorite_mode: set[str] = set()

    players = set(data["players"])
    print(f"Unique players: {players}")

    achievements = {achievement for achievement in data["achievements"]}
    print(f"Unique achivements: {achievements}")

    favorite_mode = {
            type["favorite_mode"]
            for type in data["players"].values()
        }
    print(f"Favorite modes: {favorite_mode}\n")


def comb_analysis(data: dict[str, Any]) -> None:

    scores = [p["total_score"] for p in data["players"].values()]

    total_players = len(data["players"])
    total_achievements = len(data["achievements"])
    avg_score = sum(scores) / len(scores)

    top_player = max(
        data["players"].items(),
        key=lambda item: item[1]["total_score"]
    )

    name, info = top_player

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {name} "
          f"({info['total_score']} points, "
          f"{info['achievements_count']} achievements)")


def main() -> None:
    data: dict[str, Any] = {}

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    list_comprehensions(data)

    print("=== Dict Comprehension Examples ===")
    dict_comprehensions(data)

    print("=== Set Comprehension Examples ===")
    set_comprehensions(data)

    print("=== Combined Analysis ===")
    comb_analysis(data)


if __name__ == "__main__":
    main()
