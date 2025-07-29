from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.motion.logic.reachable import Reachable
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece

if TYPE_CHECKING:
    from chess.rank.rank import Rank


class MotionService(ABC):
    _logic: Reachable
    _search_pattern: SearchPattern

    def __init__(self, logic: Reachable, search_pattern: SearchPattern):
        if logic is None:
            raise ValueError("MotionService logic cannot be None.")
        if search_pattern is None:
            raise ValueError("Search pattern cannot be None.")

        self._logic = logic
        self._search_pattern = search_pattern

    @property
    def logic(self) -> Reachable:
        return self._logic

    @property
    def search_pattern(self) -> SearchPattern:
        return self._search_pattern

    # Final method — performs common validation before deferring to subclass logic
    def dispatch_to_move_executor(self, piece: Piece, destination: Coordinate, board: Board):
        self._validate(piece, board)
        self._validate_destination(destination, board)
        self._execute_move(piece, destination, board)

    # Final method — performs common validation before deferring to subclass logic
    def explore(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        return self._perform_exploration(piece, board)

    @abstractmethod
    def _execute_move(self, piece: 'Piece', destination: Coordinate, board: Board):
        raise NotImplementedError("Subclasses must implement _perform_move.")

    @abstractmethod
    def _perform_exploration(self, piece: 'Piece', board: Board) -> List[Coordinate]:
        raise NotImplementedError("Subclasses must implement _perform_explore.")

    def _validate(self, piece: Piece,  board: Board):
        if piece is None:
            raise ValueError("Cannot move a piece that does not exist.")
        if piece.current_position() is None:
            raise ValueError(f"Before {piece.label} can be moved it has to be placed in its starting positon.")
        if board is None:
            raise ValueError(f"Cannot move {piece.label} the board does not exist.")

    def _validate_destination(self, destination: Coordinate, board: Board):
        if not board.coordinate_is_valid(destination):
            raise ValueError(f"Destination coordinate {destination} is invalid.")
