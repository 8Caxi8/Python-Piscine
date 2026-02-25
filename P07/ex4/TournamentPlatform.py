from .TournamentCard import TournamentCard
from abc import ABC
from ex0.Card import CardError


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self._cards.update({card.id: card})
        interfaces = [parent.__name__
                      for parent in TournamentCard.__mro__[1:]
                      if parent not in (object, ABC)
                      ]
        card_info = card.get_rank_info()

        return (f"{card.name} (ID: {card.id}):\n"
                f"- Interfaces: {interfaces}\n"
                f"- Rating: {card_info['Rating']}\n"
                f"- Record: {card_info['Record']}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        while True:
            result = self._cards[card1_id].attack(self._cards[card2_id])
            if not result["still_alive"]:
                winner = self._cards[card1_id]
                loser = self._cards[card2_id]
                break

            result = self._cards[card2_id].attack(self._cards[card1_id])
            if not result["still_alive"]:
                winner = self._cards[card2_id]
                loser = self._cards[card1_id]
                break

        try:
            winner_wins = str(winner.get_rank_info()["Record"]).split("-")[0]
            winner.update_wins(int(winner_wins) + 1)

            loser_losses = str(loser.get_rank_info()["Record"]).split("-")[1]
            loser.update_losses(int(loser_losses) + 1)

        except ValueError as e:
            raise CardError(e)
        self._matches += 1

        return {
            "winer": card1_id,
            "loser": card2_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        all_cards = [self._cards[id] for id in self._cards.keys()]
        all_cards.sort(key=lambda all_cards: all_cards.wins, reverse=True)
        return [f"{card.name} - Rating: {card.get_rank_info()['Rating']}"
                f"({card.get_rank_info()['Record']})" for card in all_cards]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        try:
            avg_rating = (sum(card.get_rank_info()["Rating"]
                          for card in self._cards.values()) / total_cards)
        except ZeroDivisionError as e:
            raise CardError(e)
        return {
            "total_cards": total_cards,
            "matches_played": self._matches,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
