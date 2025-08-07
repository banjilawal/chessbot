from abc import ABC, abstractmethod
from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.walk import Walk
from chess.motion.abstract.search_pattern import SearchPattern
from chess.team.model.piece import ChessPiece


class MotionController(ABC):
    _name: str
    _letter: str
    _logic: Walk
    _search_pattern: SearchPattern
    _capture_value: int
    _number_per_team: int
    _territories: List[Quadrant]

    def __init__(
        self,
        name: str,
        letter: str,
        logic: Walk,
        search_pattern:SearchPattern,
        capture_value: int,
        number_per_team: int,
        territories: List[Quadrant]
    ):
        if logic is None:
            raise ValueError("Walk logic cannot be None.")
        if search_pattern is None:
            raise ValueError("Search pattern cannot be None.")

        self._name = name
        self._logic = logic
        self._letter = letter
        self._search_pattern = search_pattern
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
    def logic(self) -> Walk:
        return self._logic

    @property
    def search_pattern(self) -> SearchPattern:
        return self._search_pattern


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
                f"num_per_player:{self._number_per_team} num_territories:{len(self._territories)}")


    def delegate_move_execution(self, piece: ChessPiece, square_service: 'ChessBoard', destination: 'Coordinate'):
        """Move a chess_piece to the specified destination."""
        if piece is None:
            raise ValueError("Cannot move a null chess_piece")
        if piece.current_coordinate() is None:
            raise ValueError(f"{piece.label} when its coord is null. It's not even on the chess_board.")
        if square_service is None:
            raise ValueError(f"{piece.label} cannot move without a chess_board.")
        if destination is None:
            raise ValueError(f"{piece.label} without a destination.")

        origin = piece.current_coordinate()
        print(f"{piece.label} starting move from {origin} to {destination}")
        print(f"motion instance: {self.motion_service}")
        print(f"motion type: {type(self.motion_service)}")
        print(f"dispatch_to_move_executor: {self.motion_service.dispatch_to_move_executor}")
        # Call motion_service.move() with keyword arguments to ensure proper parameter alignment
        self.motion_service.dispatch_to_move_executor(piece, destination, square_service)


    def explore(self, piece: ChessPiece, board: 'ChessBoard') -> List['Coordinate']:
        """Find all possible moves for a bishop chess_piece."""
        if piece is None:
            raise ValueError("BishopMotionController cannot explore without a chess_piece.")

        if board is None:
            raise ValueError("BishopMotionController cannot explore without a chess_board.")

        return self.motion_service.explore(piece, board)

    def __str__(self):
        return (f"{self._name}, value:{self._letter}, {self._capture_value} "
                f"num_per_player:{self._number_per_team} num_territories:{len(self._territories)}")

    def validate_and_check_move(self, piece: 'ChessPiece', board: 'ChessBoard', destination: 'Coordinate'):
        """
        Validates a move for a chess piece. This method performs general checks
        and then delegates to _apply_move_logic for piece-specific validation.
        It does NOT modify the board state. It raises ValueError if the move is invalid.
        """
        if piece is None:
            raise ValueError("Cannot validate move for a chess_piece that does not exist.")
        if piece.current_coordinate() is None:
            raise ValueError(f"Before {piece.label} can be moved it has to be placed in its starting position.")
        if board is None:
            raise ValueError(f"Cannot validate move for {piece.label} as the board does not exist.")
        if destination is None:
            raise ValueError(f"{piece.label} move without a destination.")
        if not board.coordinate_is_valid(destination):
            raise ValueError(f"Destination coordinate {destination} is invalid.")

        # Delegate to piece-specific logic for detailed validation
        self._apply_move_logic(piece, board, destination)


    def get_legal_moves(self, piece: 'ChessPiece', board: 'ChessBoard') -> List['Coordinate']:
        """
        Finds all legal destination coordinates for the given chess piece.
        This method is for exploring possible moves on the board.
        """
        self._validate_explore_parameters(piece, board)
        return self._generate_moves_from_pattern(piece, board)

    @abstractmethod
    def _apply_move_logic(self, piece: 'ChessPiece', board: 'ChessBoard', destination: 'Coordinate'):
        """
        Subclasses implement the specific logic for validating a move for the piece.
        This method should raise ValueError if the move is invalid (e.g., geometrically unreachable,
        destination occupied by friendly piece, path blocked).
        It should NOT modify the board state.
        """
        pass

    @abstractmethod
    def _generate_moves_from_pattern(self, piece: 'ChessPiece', board: 'ChessBoard') -> List['Coordinate']:
        """
        Subclasses implement the specific logic for generating possible moves.
        """
        pass

    def _validate_explore_parameters(self, piece: 'ChessPiece', board: 'ChessBoard'):
        if piece is None:
            raise ValueError("Cannot explore moves for a chess_piece that does not exist.")
        if board is None:
            raise ValueError("Cannot explore moves without a board.")

