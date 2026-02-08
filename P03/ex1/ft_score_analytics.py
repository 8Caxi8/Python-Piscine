import sys


def score_analytics() -> None:
    scores: list[int] = []
    score: int
    args: list[str] = sys.argv[1:]

    if not args:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...\n")
        return

    for arg in args:
        try:
            score = int(arg)
        except ValueError:
            print(f"Error: '{arg}' is not a valid number!")
            return
        scores.append(score)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


def main() -> None:
    print("=== Player Score Analytics ===")
    score_analytics()


if __name__ == "__main__":
    main()
