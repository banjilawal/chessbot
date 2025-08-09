from typing import List, Optional, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.board.element.square import Square
from chess.board.square_iterator import SquareIterator

if TYPE_CHECKING:
    from chess.token.piece import ChessPiece


class Map:
    """
    A repository for managing all the squares on the chess map_service.
    It provides methods for finding squares and iterating over them.
    """
    _squares: List[List[Square]]

    def __init__(self, squares: List[List[Square]]):
        """
        Initializes the Map with a 2D list of Square objects.

        Args:
            squares: A list of lists representing the rows and columns of the map_service.
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
        Returns a SquareIterator for traversing the map_service.

        Args:
            index: The starting coordinate for the iteration.
            delta: The direction of the iteration.
        """
        return SquareIterator(self._squares, index, delta)

    def occupied_squares(self) -> List[Square]:
        """Returns a list of all squares that are currently occupied by a chess_piece."""
        return [square for row in self._squares for square in row if square.occupant is not None]

    def empty_squares(self) -> List[Square]:
        """Returns a list of all squares that are currently vacant."""
        return [square for row in self._squares for square in row if square.occupant is None]


    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        """
        Finds a board by its coordinate.

        Args:
            coordinate: The Coordinate object of the board.

        Returns:
            The Square object if found, otherwise None.
        """
        if 0 <= coordinate.row < len(self._squares) and 0 <= coordinate.column < len(self._squares[0]):
            return self._squares[coordinate.row][coordinate.column]
        return None


    def find_square_by_name(self, name: str) -> Optional[Square]:
        """
        Finds a board by its algebraic notation name (e.g., "a1").

        Args:
            name: The name of the board to find.

        Returns:
            The Square object if found, otherwise None.
        """
        for row in self._squares:
            for square in row:
                if square.name.upper() == name.upper():
                    return square
        return None

    def find_square_by_id(self, square_id: int) -> Optional[Square]:
        """
        Finds a board by its unique ID.
        Args:
            square_id: The ID of the board to find.
        Returns:
            The Square object if found, otherwise None.
        """
        for row in self._squares:
            for square in row:
                if square.id == square_id:
                    return square
        return None


    def chess_piece(self, coordinate: Coordinate) -> Optional['ChessPiece']:
        """
        Returns the chess chess_piece at a given coordinate.
        Args:
            coordinate: The coordinate to check.
        Returns:
            The ChessPiece object if a chess_piece is on the board, otherwise None.
        """
        square = self.find_square_by_coordinate(coordinate)
        return square.occupant if square else None


    def capture_square(self, chess_piece: 'ChessPiece', destination: Coordinate):

        destination_square = self.find_square_by_coordinate(destination)
        target_occupant = destination_square.occupant

        if target_occupant is None or chess_piece.is_enemy(target_occupant):
            self._capture_helper(chess_piece, destination_square, target_occupant)
        else:
            print("The square is occupied by a friendly")
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
                "Fatal error. A friendly should never be a self._capture_helper parameter."
            )

        if enemy is not None:
            chess_piece.capture_prisoner(enemy)

        originating_square.set_occupant(None)
        target_square.set_occupant(chess_piece)
        chess_piece.coordinate_stack.push_coordinate(target_square.coordinate)


    def __str__(self) -> str:
        """
        Provides a string representation of the map_service, showing pieces or board names.

        If a board is occupied, it shows the chess chess_piece's name.
        If a board is vacant, it shows the board's name in brackets.
        """
        string = ""
        # Iterate from the top row (row 7) down to the bottom (row 0)
        for row in reversed(self._squares):
            row_str_parts = []
            for square in row:
                if square.occupant is not None:
                    # Display the chess_piece's name if the board is occupied.
                    row_str_parts.append(f"[{square.occupant.name}]")
                else:
                    # Display the board's name in brackets if it's empty.
                    row_str_parts.append(f"[{square.name}]")
            string += " ".join(row_str_parts) + "\n"
        return string.strip()




