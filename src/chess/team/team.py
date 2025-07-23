from dataclasses import field
from typing import Dict, Optional, List

from chess.common.config import ChessPieceConfig
from chess.piece.chess_piece import ChessPiece
from chess.team.home import TeamHome
from podscape.constants import GameColor

class Team:
    _id: int
    _color: GameColor
    _home: TeamHome
    _captives:List[ChessPiece] = field(default_factory=list)
    _piece_registry: Dict[ChessPieceConfig, Dict[int, Optional[ChessPiece]]] = field(init=False)

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
    def captives(self) -> List[ChessPiece]:
        return List(self._captives)
    @property
    def piece_registry(self) -> Dict[int, Optional[ChessPiece]]:
        return Dict(self._piece_registry)
