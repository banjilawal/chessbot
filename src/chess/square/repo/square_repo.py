from typing import List, Optional


from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.team.model.piece import ChessPiece
from chess.square.model.square import Square
from chess.square.repo.iterator import SquareIterator


class SquareRepo:
    """
    A repository for managing all the squares on the chess board.
    It provides methods for finding squares and iterating over them.
    """
    _squares: List[List[Square]]

    def __init__(self, squares: List[List[Square]]):
        """
        Initializes the SquareRepo with a 2D list of Square objects.

        Args:
            squares: A list of lists representing the rows and columns of the board.
        """
        self._squares = squares

    @property
    def squares(self) -> List[List[Square]]:
        """Returns the 2D list of squares."""
        return self._squares

    def iterator(
        self,
        index: Coordinate = Coordinate(0, 0),
        delta: Delta = Delta(delta_column=1, delta_row=1)
     ) -> SquareIterator:
        """
        Returns a SquareIterator for traversing the board.

        Args:
            index: The starting coordinate for the iteration.
            delta: The direction of the iteration.
        """
        return SquareIterator(self._squares, index, delta)

    def occupied_squares(self) -> List[Square]:
        matches: List[Square] = []
        for row in self._squares:
            for square in row:
                if square.occupant is not None and square not in matches:
                    matches.append(square)
        return matches

    def empty_squares(self) -> List[Square]:
        matches: List[Square] = []
        for row in self._squares:
            for square in row:
                if square.occupant is None and square not in matches:
                    matches.append(square)
        return matches


    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        """
        Finds a square by its coordinate.

        Args:
            coordinate: The Coordinate object of the square.

        Returns:
            The Square object if found, otherwise None.
        """
        # Corrected to return the square.
        return self._squares[coordinate.row][coordinate.column]

    def find_square_by_name(self, name: str) -> Optional[Square]:
        """
        Finds a square by its algebraic notation name (e.g., "a1").

        Args:
            name: The name of the square to find.

        Returns:
            The Square object if found, otherwise None.
        """
        for row in self._squares:
            for square in row:
                if square.name == name:
                    return square
        return None

    def find_square_by_id(self, square_id: int) -> Optional[Square]:
        """
        Finds a square by its unique ID.

        Args:
            square_id: The ID of the square to find.

        Returns:
            The Square object if found, otherwise None.
        """
        for row in self._squares:
            for square in row:
                if square.id == square_id:
                    return square
        return None

    def chess_piece(self, coordinate: Coordinate) -> Optional[ChessPiece]:
        """
        Returns the chess piece at a given coordinate.

        Args:
            coordinate: The coordinate to check.

        Returns:
            The ChessPiece object if a piece is on the square, otherwise None.
        """
        # This implementation is inefficient as it iterates the whole board.
        # A more efficient approach would be to use find_square_by_coordinate first.
        square = self.find_square_by_coordinate(coordinate)
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




