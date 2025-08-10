from typing import List, Optional

from chess.arena.arena import Arena
from chess.game.game import Game
from chess.owner.owner import Owner


class GameRepo:
    _chess_pieces: List[Game]

    def __init__(self,):
        self._games = []


    def add(self, game: Game):
        if game not in self._games and game is not None:
            self._chess_pieces.append(game)


    def find(self, game_id: int) -> Optional[Game]:
        for game in self._games:
            if game.id == game_id:
                return game
        return None


    def filter_by_winner(self, winner: Owner) -> List[Game]:
        matches: List[Game] = []

        for game in self._games:
            if game.winner == winner and game not in matches:
                matches.append(game)
        return matches


    def filter_by_arena(self, arena: Arena) -> List[Game]:
        matches: List[Game] = []

        for game in self._games:
            if game.arena == arena and game not in matches:
                matches.append(game)
        return matches

