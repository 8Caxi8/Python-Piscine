def list_comprehensions(data: dict) -> None:
    high_scores: list[int] = []
    high_scorers: list[str] = []
    active_players: list[int] = []

    high_scorers = (
        player
        for player, value in data["players"].items()
        if value["total_score"] > 2000)
    print(f"High scorers (>2000): {list(high_scorers)}")

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


def dict_comprehensions(data: dict) -> None:
    player_scores: dict = dict()
    categories: dict = dict()
    count_scores: dict = dict()

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


def set_comprehensions(data: dict) -> None:
    players: set = set()
    achievements: set = set()
    favorite_mode: set = set()

    players = {player for player in data["players"].keys()}
    print(f"Unique players: {players}")

    achievements = {achievement for achievement in data["achievements"]}
    print(f"Unique achivements: {achievements}")

    favorite_mode = {
            type["favorite_mode"]
            for type in data["players"].values()
        }
    print(f"Favorite modes: {favorite_mode}\n")


def comb_analysis(data: dict) -> None:
    no_players: int
    high_scores: list
    scores_normalized: list
    top_performer: dict

    no_players = len({player for player in data["players"].keys()})
    print(f"Total Players: {no_players}")

    high_scores = [
        value["total_score"]
        for value in data["players"].values()
        if value["total_score"] > 2000]

    scores_normalized = [
        int(value["total_score"] / max(high_scores) * 100)
        for value in data["players"].values()]
    print(f"Normalized scores: {scores_normalized}")

    top_performer = max(
        data["players"],
        key=lambda p: data["players"][p]["total_score"])
    print(f"Top performer: {top_performer}\n")


def analytics_dashboard(data: dict) -> None:
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
    data: dict = dict()
    analytics_dashboard(data)
