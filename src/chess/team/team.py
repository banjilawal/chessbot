from dataclasses import field
from typing import Dict, Optional, List

from chess.common.config import ChessPieceConfig
from chess.common.constant import GameColor
from chess.common.geometry import Quadrant
from chess.common.piece import Piece

class Team:
    _id: int
    _home_quadrant: Quadrant
    _members: List[Piece]

    def __init__(self, team_id: int, home_quadrant: Quadrant, members: List[Piece]):
        self._id = team_id
        self._home_quadrant = home_quadrant
        for member in members:
            self._members.append(member)


    @property
    def id(self) -> int:
        return self._id


    @property
    def quadrant(self):
        return self._home_quadrant


    @property
    def members(self) -> List[Piece]:
        return self._members.copy()


    @property
    def piece_registry(self) -> Dict[int, Optional[Piece]]:
        return Dict(self._piece_registry)


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Team):
            return False
        return self._id == other.id