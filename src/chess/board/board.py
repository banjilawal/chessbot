import random
from sys import deactivate_stack_trampoline
from typing import List, Optional, TYPE_CHECKING

from chess.board import square
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
        if name is None:
            raise Exception(f"Cannot find a square with a null name")

        for row in self._squares:
            for current_square in row:
                if current_square.name.upper() == name.upper():
                    return current_square
        return None

    def find_square_by_id(self, square_id: int) -> Optional[Square]:
        if square_id is None:
            raise Exception(f"Cannot find a square with a null id")

        if square_id < 0:
            raise Exception(f"find_square_by_id: square_id {square_id} is negative")

        for row in self._squares:
            for current_square in row:
                if current_square.id == square_id:
                    return current_square
        return None


    def find_chess_piece(self, coordinate: Coordinate) -> Optional['ChessPiece']:
        if coordinate is None:
            raise Exception(f"Cannot find a chess piece with a null coordinate")
        if coordinate.row < 0 or coordinate.row >= len(self._squares):
            raise Exception(f"find_chess_piece: coordinate row {coordinate.row} is out of range")
        if coordinate.column < 0 or coordinate.column >= len(self._squares[0]):
            raise Exception(f"find_chess_piece: coordinate column {coordinate.column} is out of range")

        return  self.find_square_by_coordinate(coordinate).occupant



    def capture_square(self, chess_piece: 'ChessPiece', destination: Coordinate):
        method = f"ChessBoard.capture_square"

        if chess_piece is None:
            raise Exception(f"{method}: chess_piece is None")

        if chess_piece.coordinate_stack.current_coordinate() is None:
            raise Exception(f"{method}: chess_piece cannot move to a location if its not on th board")

        if self.find_square_by_coordinate(destination) is None:
            raise Exception(f"{method}: coordinate {destination} is not on the board")

        destination_square = self.find_square_by_coordinate(destination)
        target_occupant = destination_square.occupant

        if target_occupant is None:
            print(
                f"{method}: "
                f"destination square {destination_square.name}"
                f" is empty calling ChessBoard._finalize_capture"
            )
            self._finalize_capture(chess_piece, destination_square)
            return

        if not chess_piece.is_enemy(target_occupant):
            print(
                f"{method}: "
                f"destination square {destination_square.name}"
                f" is occupied by friend{target_occupant.name} "
                f"mark as obstruction"
            )
            chess_piece.add_obstruction(target_occupant)
            return


        if chess_piece.is_enemy(target_occupant):
            print(
                f"current occupant {target_occupant.name} "
                f"is being captured by its enemy {chess_piece.name} "
                f"calling ChesBoard.take_prisoner"
            )
            self._imprison_occupant(chess_piece, target_occupant)
            self._finalize_capture(chess_piece, destination_square)
            return
            # print(f"From BAORD.capture_square destination square is {destination_square}")
            # self._capture_helper(chess_piece, destination_square, target_occupant)


    def _imprison_occupant(self, jailer: 'ChessPiece', prisoner: 'ChessPiece'):
        self.find_square_by_coordinate(prisoner.coordinate_stack.current_coordinate()).occupant = None
        prisoner.captor = jailer



    def _finalize_capture(self, chess_piece: 'ChessPiece', destination_square: Square):
        method = f"ChessBoard._finalize_capture"

        destination_square.occupant = chess_piece
        self.find_square_by_coordinate(
            chess_piece.coordinate_stack.current_coordinate()
        ).occupant

        chess_piece.coordinate_stack.push_coordinate(destination_square.coordinate)

        if destination_square.occupant is not chess_piece:
            raise Exception(f"{method}: data inconsistency square occupant not updated")
        if chess_piece.coordinate_stack.current_coordinate() is not destination_square.coordinate:
            raise Exception(f"{method}: chess_piece coordinate stack not updated")

        print(f"{method}: capture complete")


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



