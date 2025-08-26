from typing import List

from chess.geometry.coordinate.coord import Coordinate
from chess.board.square import Square
from chess.geometry.vector.algebra import VectorAlgebra
from chess.geometry.vector.delta import Vector


class SquareIterator:
    _vector: Vector
    _squares: List[List[Square]]
    _coord: Coordinate

    def __init__(self, vector: Vector, squares: List[List[Square]], coord: Coordinate = Coordinate(0, 0)):
        self._vector = vector
        self._squares = squares
        self._coord = coord


    def __iter__(self) -> 'SquareIterator':
        return self


    def __next__(self) -> Square:
        if self._coord.row >= len(self._squares) or self._coord.column >= len(self._squares[0]):
            raise StopIteration

        next_square = self._squares[self._coord.row][self._coord.column]
        self._coord = VectorAlgebra.add_vector_to_coordinate(self._coord, self._vector)
        return next_square