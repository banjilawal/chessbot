from dataclasses import field
from typing import Dict, Optional, List

from chess.common.config import ChessPieceConfig
from chess.common.constant import GameColor
from chess.piece.piece import Piece
from chess.team.home import TeamHome

class Team:
    _id: int
    _color: GameColor
    _home: TeamHome
    _captives:List[Piece] = field(default_factory=list)
    _piece_registry: Dict[ChessPieceConfig, Dict[int, Optional[Piece]]] = field(init=False)

    def __init__(self, team_id: int, color: GameColor, home:TeamHome):
        self._id = team_id
        self._color = color
        self._home = home

    @property
    def id(self) -> int:
        return self._id
    @property
    def color(self) -> GameColor:
        return self._color
    @property
    def home(self) -> TeamHome:
        return self._home
    @property
    def captives(self) -> List[Piece]:
        return List(self._captives)
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
        return self._id == other.id and self._color == other.color and self._home == other.home