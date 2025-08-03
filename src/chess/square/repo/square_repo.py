from typing import List, Optional


from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.piece.piece import ChessPiece
from chess.square.model.square import Square
from chess.square.repo.iterator import SquareIterator


class SquareRepo:
    _squares: List[List[Square]]


    def __init__(self, squares: List[List[Square]]):
        self._squares = squares


    @property
    def squares(self) -> List[List[Square]]:
        return self._squares


    def iterator(
        self,
        index: Coordinate = Coordinate(0, 0),
        delta: Delta=Delta(delta_column=1, delta_row=1)
     ) -> SquareIterator:
        return SquareIterator(self._squares, index, delta)


    def square(self, coordinate: Coordinate) -> Optional[Square]:
        square = self._squares[coordinate.row][coordinate.column]



    def chess_piece(self, coordinate) -> Optional[ChessPiece]:
        return self._square(coordinate).occupant



    def __str__(self) -> str:
        string = ""
        for row_index in reversed(range(len(self._squares))):  # start from top row (8) to bottom (1)
            row_squares = self._squares[row_index]
            row_str = " ".join(f"[{square.name}]" for square in row_squares)
            string += row_str + "\n"
        return string.strip()




