from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.pawn_defintion import PawnDefinition
from chess.team.home import TeamHome


class PawnCaptureEnemyDefinition(PawnDefinition):
    _pawn_home: TeamHome
    _board: Board

    def __init__(self, definition_id, title, team: TeamHome, board: Board):
        super().__init__(definition_id, title)
        self._pawn_home = team
        self._board = board

    @property
    def pawn_home(self) -> TeamHome:
        return self._pawn_home

    @property
    def board(self) -> Board:
        return self._board


    def can_capture_enemy(
        self,
        origin: Coordinate,
        destination: Coordinate,
        pawn_home: Optional[TeamHome]
    ) -> bool:
        if pawn_home is None:
        if origin is None:
            return False
        if destination is None:
            return False
        if destination.row != origin.row + 1:
            return False
        if destination.column + 1 == origin.column or origin.column + 1 == destination.column:
            return False
        occupant = self.board.get_chess_piece_by_coordinate(destination)
        if occupant is None:
            return False
        if occupant.team.home == pawn_home:
            return False
        if occupant.team != self.pawn_home:
            return True
        return False