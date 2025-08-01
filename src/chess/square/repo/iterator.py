from typing import List

from chess.geometry.board.coordinate import Coordinate, Delta
from chess.square.model.square import Square


class SquareIterator:
    _squares: List[List[Square]]
    _index: Coordinate
    _delta: Delta

    def __init__(
        self,
        squares: List[List[Square]],
        index: Coordinate = Coordinate(0, 0),
        delta: Delta=Delta(delta_column=1, delta_row=1)
    ):
        self._squares = squares
        self._index = index
        self._delta = delta

    def __iter__(self) -> 'SquareIterator':
        return self

    def __next__(self) -> Square:
        if self._index.rows >= len(self._squares) or self._index.columns >= len(self._squares[0]):
            raise StopIteration

        next_square = self._squares[self._index.rows][self._index.columns]
        self._index = self._index.shift(self._delta)
        return next_square