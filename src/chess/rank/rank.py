from abc import ABC, abstractmethod
from typing import List, Optional

from chess.geometry.board import ChessBoard
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.service.motion_service import MotionService
from chess.piece.piece import ChessPiece
from chess.game.record.turn_record import TurnRecord


class Rank(ABC):
    _name: str
    _acronym: str
    _motion: MotionService
    _capture_value: int
    _members: List[ChessPiece]
    _territories: List[Quadrant]

    def __init__(
        self, 
        name: str, 
        acronym: str, 
        motion: MotionService,
        capture_value: int, 
        territories: List[Quadrant]
    ):
        self._name = name
        self._members = []
        self._motion = motion
        self._acronym = acronym
        self._capture_value = capture_value
        self._territories = territories


    @property
    def name(self) -> str:
        return self._name


    @property
    def acronym(self) -> str:
        return self._acronym
    
    @property
    def motion(self):
        return self._motion


    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()

    @property
    def members(self) -> [ChessPiece]:
        return self._members

    @property
    def acronym(self) -> str:
        return self._acronym

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Rank):
            return False
        return self._name == other.name

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return (f"{self._name}, value:{self._acronym}, {self._capture_value} "
                f"num_members:{len(self._members)} num_territories:{len(self._territories)}")


    def delegate_move_excution(self, piece: ChessPiece, board: 'ChessBoard', destination: 'Coordinate'):
        """Move a chess_piece to the specified destination."""
        if piece is None:
            raise ValueError("Cannot move a null chess_piece")
        if piece.current_coordinate() is None:
            raise ValueError(f"{piece.label} when its coord is null. It's not even on the chess_board.")
        if board is None:
            raise ValueError(f"{piece.label} cannot move without a chess_board.")
        if destination is None:
            raise ValueError(f"{piece.label} without a destination.")

        origin = piece.current_coordinate()
        print(f"{piece.label} starting move from {origin} to {destination}")
        print(f"motion instance: {self.motion}")
        print(f"motion type: {type(self.motion)}")
        print(f"dispatch_to_move_executor: {self.motion.dispatch_to_move_executor}")
        # Call motion.move() with keyword arguments to ensure proper parameter alignment
        self.motion.dispatch_to_move_executor(piece, destination, board)


    def explore(self, piece: ChessPiece, board: 'ChessBoard') -> List['Coordinate']:
        """Find all possible moves for a bishop chess_piece."""
        if piece is None:
            raise ValueError("Bishop cannot explore without a chess_piece.")

        if board is None:
            raise ValueError("Bishop cannot explore without a chess_board.")

        return self.motion.explore(piece, board)


