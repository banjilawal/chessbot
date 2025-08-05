from abc import ABC
from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.motion_service import MotionService
from chess.piece.piece import ChessPiece


class MotionController(ABC):
    _name: str
    _letter: str
    _motion_service: MotionService
    _capture_value: int
    _number_per_player: int
    _territories: List[Quadrant]

    def __init__(
        self,
        name: str,
        letter: str,
        motion_service: MotionService,
        capture_value: int,
        number_per_player: int,
        territories: List[Quadrant]
    ):
        self._name = name
        self._members = []
        self._motion_service = motion_service
        self._letter = letter
        self._capture_value = capture_value
        self._number_per_player = number_per_player
        self._territories = territories


    @property
    def name(self) -> str:
        return self._name


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def motion_service(self):
        return self._motion_service


    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()

    @property
    def number_per_player(self) -> int:
        return self._number_per_player


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, MotionController):
            return False
        return self._name == other.name

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return (f"{self._name}, value:{self._letter}, {self._capture_value} "
                f"num_per_player:{self._number_per_player} num_territories:{len(self._territories)}")


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
        print(f"motion instance: {self.motion_service}")
        print(f"motion type: {type(self.motion_service)}")
        print(f"dispatch_to_move_executor: {self.motion_service.dispatch_to_move_executor}")
        # Call motion_service.move() with keyword arguments to ensure proper parameter alignment
        self.motion_service.dispatch_to_move_executor(piece, destination, board)


    def explore(self, piece: ChessPiece, board: 'ChessBoard') -> List['Coordinate']:
        """Find all possible moves for a bishop chess_piece."""
        if piece is None:
            raise ValueError("Bishop cannot explore without a chess_piece.")

        if board is None:
            raise ValueError("Bishop cannot explore without a chess_board.")

        return self.motion_service.explore(piece, board)


