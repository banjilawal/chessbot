from abc import ABC
from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.motion.interfaces.explorer import Explorer
from chess.motion.walk.walk import Walk


class MotionController(ABC):
    _name: str
    _letter: str
    _walk: Walk
    _explorer: Explorer
    _capture_value: int
    _number_per_team: int
    _territories: List[Quadrant]

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value: int,
        number_per_team: int,
        territories: List[Quadrant],
        walk: Optional[Walk] = None,
        explorer:Optional[Explorer] = None
    ):
        if walk is None:
            raise ValueError("Walk walk cannot be None.")
        if explorer is None:
            raise ValueError("Search pattern cannot be None.")

        self._name = name
        self._walk = walk
        self._letter = letter
        self._explorer = explorer
        self._capture_value = capture_value
        self._number_per_team = number_per_team
        self._territories = territories


    @property
    def name(self) -> str:
        return self._name


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def capture_value(self) -> int:
        return self._capture_value


    @property
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()


    @property
    def number_per_team(self) -> int:
        return self._number_per_team


    @property
    def walk(self) -> Walk:
        return self._walk


    @property
    def explorer(self) -> Explorer:
        return self._explorer


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, MotionController):
            return False
        return self._name.upper() == other.name.upper()


    def __hash__(self):
        return hash(self._name)


    def __str__(self):
        return (f"{self._name}, value:{self._letter}, {self._capture_value} "
                f"num_per_player:{self._number_per_team} num_territories:{len(self._territories)}")

    #
    # def delegate_move_execution(self, chess_piece: ChessPiece, square_service: 'ChessBoard', destination: 'Coordinate'):
    #     """Move a chess_piece to the specified destination."""
    #     if chess_piece is None:
    #         raise ValueError("Cannot move a null chess_piece")
    #     if chess_piece.current_coordinate() is None:
    #         raise ValueError(f"{chess_piece.label} when its coord is null. It's not even on the chess_board.")
    #     if square_service is None:
    #         raise ValueError(f"{chess_piece.label} cannot move without a chess_board.")
    #     if destination is None:
    #         raise ValueError(f"{chess_piece.label} without a destination.")
    #
    #     origin = chess_piece.current_coordinate()
    #     print(f"{chess_piece.label} starting move from {origin} to {destination}")
    #     print(f"motion instance: {self.motion_service}")
    #     print(f"motion type: {type(self.motion_service)}")
    #     print(f"dispatch_to_move_executor: {self.motion_service.dispatch_to_move_executor}")
    #     # Call motion_service.move() with keyword arguments to ensure proper parameter alignment
    #     self.motion_service.dispatch_to_move_executor(chess_piece, destination, square_service)
    #
    #
    # def explore(self, chess_piece: ChessPiece, board: 'ChessBoard') -> List['Coordinate']:
    #     """Find all possible moves for a bishop chess_piece."""
    #     if chess_piece is None:
    #         raise ValueError("BishopMotionController cannot explore without a chess_piece.")
    #
    #     if board is None:
    #         raise ValueError("BishopMotionController cannot explore without a chess_board.")
    #
    #     return self.motion_service.explore(chess_piece, board)
    #
    # def __str__(self):
    #     return (f"{self._name}, value:{self._letter}, {self._capture_value} "
    #             f"num_per_player:{self._number_per_team} num_territories:{len(self._territories)}")
    #
    # def validate_and_check_move(self, chess_piece: 'ChessPiece', board: 'ChessBoard', destination: 'Coordinate'):
    #     """
    #     Validates a move for a chess chess_piece. This method performs general checks
    #     and then delegates to _apply_move_logic for chess_piece-specific validation.
    #     It does NOT modify the board state. It raises ValueError if the move is invalid.
    #     """
    #     if chess_piece is None:
    #         raise ValueError("Cannot validate move for a chess_piece that does not exist.")
    #     if chess_piece.current_coordinate() is None:
    #         raise ValueError(f"Before {chess_piece.label} can be moved it has to be placed in its starting position.")
    #     if board is None:
    #         raise ValueError(f"Cannot validate move for {chess_piece.label} as the board does not exist.")
    #     if destination is None:
    #         raise ValueError(f"{chess_piece.label} move without a destination.")
    #     if not board.coordinate_is_valid(destination):
    #         raise ValueError(f"Destination coordinate {destination} is invalid.")
    #
    #     # Delegate to chess_piece-specific walk for detailed validation
    #     self._apply_move_logic(chess_piece, board, destination)
    #
    #
    # def get_legal_moves(self, chess_piece: 'ChessPiece', board: 'ChessBoard') -> List['Coordinate']:
    #     """
    #     Finds all legal destination coordinates for the given chess chess_piece.
    #     This method is for exploring possible moves on the board.
    #     """
    #     self._validate_explore_parameters(chess_piece, board)
    #     return self._generate_moves_from_pattern(chess_piece, board)
    #
    #
    #
    # def _validate_explore_parameters(self, chess_piece: 'ChessPiece', board: 'ChessBoard'):
    #     if chess_piece is None:
    #         raise ValueError("Cannot explore moves for a chess_piece that does not exist.")
    #     if board is None:
    #         raise ValueError("Cannot explore moves without a board.")

