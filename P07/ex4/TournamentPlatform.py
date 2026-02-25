from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self._cards.update({card.id: card})

        return (f"{card.name} (ID: {card.id}):\n"
                "- Interfaces:"
                f"{[parent for parent in TournamentCard.__mro__[1:]]}\n"
                f"- Rating: {card.get_rank_info()["Rating"]}\n"
                f"- Record: {card.get_rank_info()["Record"]}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        winner = self._cards[card1_id]
        loser = self._cards[card2_id]

        winnerwins = str(winner.get_rank_info()["Record"]).split("-")[0]
        winner.update_wins(int(winnerwins) + 1)

        loserlosses = str(loser.get_rank_info()["Record"]).split("-")[1]
        loser.update_losses(int(loserlosses) + 1)

        self._matches += 1

        return {
            "winer": card1_id,
            "loser": card2_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        all_cards = [self._cards[id] for id in self._cards.keys()]
        all_cards.sort(key=lambda all_cards: all_cards.wins)
        return [f"{card.name} - Rating: {card.get_rank_info()["Rating"]}"
                f"({card.get_rank_info()["Record"]})" for card in all_cards]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        avg_rating = (sum(card.get_rank_info()["Rating"]
                          for card in self._cards.values()) / total_cards)
        return {
            "total_cards": total_cards,
            "matches_played": self._matches,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
