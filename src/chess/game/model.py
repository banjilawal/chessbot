from typing import List

from chess.arena.model import Arena
from chess.geometry.coordinate.coord_stack import CoordinateStack
from chess.owner.base import Owner

class Game:
    _id: int
    _arena: Arena
    _winner: Owner
    _game_Log: List[CoordinateStack]

    def __init__(self, match_id: int, arena: Arena):
        self._id = match_id
        self._arena = arena
        self._winner = None
        self._game_log = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def arena(self) -> Arena:
        return self._arena

    @property
    def winner(self) -> Owner:
        return self._winner

    @property
    def game_log(self) -> List[CoordinateStack]:
        return self._game_log