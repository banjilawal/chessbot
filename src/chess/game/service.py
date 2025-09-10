from typing import Optional, List

from chess.game.model import Game
from chess.game.repo import GameRepo
from chess.competitor.commander import Commander


class GameService:
    _repo: GameRepo

    def __init__(self, repo: GameRepo):
        self._repo = repo


    def add_game(self, game):
        self._repo.add(game)

    def find_game_by_id(self, game_id: int) -> Optional[Game]:
        return self._repo.find(game_id)

    def find_games_by_winner(self, winner: Commander) -> List[Game]:
        return self._repo.filter_by_winner(winner)