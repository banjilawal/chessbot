import random
from typing import List, Optional, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.board.square import Square
from chess.board.square_iterator import SquareIterator

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece


class ChessBoard:
    _id: int
    _squares: List[List[Square]]

    def __init__(self, board_id: int, squares: List[List[Square]]):
        self._id = board_id
        self._squares = squares


    @property
    def id(self) -> int:
        return self._id


    @property
    def squares(self) -> List[List[Square]]:
        return self._squares


    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, ChessBoard): return False
        return self._id == other.id


    def iterator(
        self,
        index: Coordinate = Coordinate(0, 0),
        delta: Delta = Delta(delta_column=1, delta_row=1)
     ) -> SquareIterator:
        """
        Returns p SquareIterator for traversing the chess_board.

        Args:
            index: The starting coordinate for the iteration.
            delta: The direction of the iteration.
        """
        return SquareIterator(self._squares, index, delta)

    def occupied_squares(self) -> List[Square]:
        return [square for row in self._squares for square in row if square.occupant is not None]

    def empty_squares(self) -> List[Square]:
        return [square for row in self._squares for square in row if square.occupant is None]


    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        if 0 <= coordinate.row < len(self._squares) and 0 <= coordinate.column < len(self._squares[0]):
            return self._squares[coordinate.row][coordinate.column]
        return None


    def find_square_by_name(self, name: str) -> Optional[Square]:
        for row in self._squares:
            for square in row:
                if square.name.upper() == name.upper():
                    return square
        return None

    def find_square_by_id(self, square_id: int) -> Optional[Square]:
        for row in self._squares:
            for square in row:
                if square.id == square_id:
                    return square
        return None


    def find_chess_piece(self, coordinate: Coordinate) -> Optional['ChessPiece']:
        square = self.find_square_by_coordinate(coordinate)
        return square.occupant if square else None


    def capture_square(self, chess_piece: 'ChessPiece', destination: Coordinate):
        destination_square = self.find_square_by_coordinate(destination)
        target_occupant = destination_square.occupant

        if target_occupant is None or chess_piece.is_enemy(target_occupant):
            self._capture_helper(chess_piece, destination_square, target_occupant)
        else:
            print("The square is occupied by p friendly")
            chess_piece.add_obstruction(target_occupant)
            return


    def _capture_helper(
        self,
        chess_piece: 'ChessPiece',
        target_square: Square,
        enemy: Optional['ChessPiece']
    ):
        originating_square = self.find_square_by_coordinate(
            chess_piece.coordinate_stack.current_coordinate()
        )

        if not chess_piece.is_enemy(enemy):
            raise Exception(
                f"{enemy} is not an enemy of "
                f"{chess_piece} who is coming from"
                f" {originating_square} to"
                f" {enemy.current_coordinate}r"
                f" Capture failed"
            )

        if enemy is not None:
            chess_piece.capture_prisoner(enemy)

        originating_square.occupant = None
        target_square.occpant = chess_piece
        chess_piece.coordinate_stack.push_coordinate(target_square.coordinate)


    def random_chess_piece(self) -> Optional['ChessPiece']:
        square = random.choice(self.occupied_squares())
        return square.occupant if square else None


    def __str__(self) -> str:
        """
        Provides a string representation of the board, showing pieces or square names.

        If a square is occupied, it shows the chess piece's name.
        If a square is vacant, it shows the square's name in brackets.
        """
        string = ""
        # Iterate from the top row (row 7) down to the bottom (row 0)
        for row in reversed(self._squares):
            row_str_parts = []
            for square in row:
                if square.occupant is not None:
                    # Display the piece's name if the square is occupied.
                    row_str_parts.append(f"[{square.occupant.name}]")
                else:
                    # Display the square's name in brackets if it's empty.
                    row_str_parts.append(f"[{square.name}]")
            string += " ".join(row_str_parts) + "\n"
        return string.strip()



