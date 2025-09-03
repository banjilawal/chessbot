from typing import List

from chess.creator.entity.builder.chess_board_builder import ChessBoardBuilder
from chess.geometry.coord import Coordinate
from chess.board.square import Square
from chess.geometry.delta import Vector


class SquareIterator:
    _vector: Vector
    _squares: List[List[Square]]
    _coord: Coordinate
    _col_vector: Vector
    _row_vector: Vector
    _square: Square
    _previous_row: int
    _previous_column: int
    _current_row: int
    _current_column: int

    def __init__(self, vector: Vector, squares: List[List[Square]], coord: Coordinate(0, 0)):
        self._vector = vector
        self._squares = squares
        self._coord = coord


        self._previous_row = self._coord.row
        self._previous_column = self._coord.column
        self._current_row = self._coord.row
        self._current_column = self._coord.column
        self._square = self._squares[self._current_row][self._current_column]


    def __iter__(self) -> 'SquareIterator':
        return self


    def _col_has_next(self) -> bool:
        # print(f"\t\tENTERED _col_has_next() with column={self._current_column}")

        if self._current_column <= len(self._squares[0])-1:
            print(f"\t\tcolumn {self._current_column} <= {len(self._squares[0])-1} returning {True}")
            return True
        else:
            print(f"\t\tcolumn {self._current_column} > {len(self._squares[0])-1} return {False}")
            return False


    def _row_has_next(self) -> bool:
        print(f"ENTERED _row_has_next() with row={self._current_row}")

        if self._current_row < len(self._squares)-1:
            print(f"\trow {self._current_row} < {len(self._squares)-1} rows returning {True}")
            # if self._col_has_next(row):
            #     self._current_column += self._vector.x
            #     # print(f"calling _col_has_next() with current_column to {self._current_column}")
            # else:
            #     print(f"\tResetting current_column from {self._current_column} to 0 to start processing row {row}")
            #     # self._current_column = 0
            return True
        else:
            print(f"\trow {self._current_row} > {len(self._squares)-1} returning {False}")
            return False

    def _has_next(self) -> bool:
        if not self._col_has_next():
            if not self._row_has_next():
                return False
            self._current_column = 0
            self._previous_row = self._current_row
            self._current_row += self._vector.y
            return True
        return True


    def __next__(self) -> Square:
        if not self._has_next():
            raise StopIteration


        self._previous_column = self._current_column
        self._current_column += self._vector.x
        self._square = self._squares[self._previous_row][self._previous_column]
        return self._square



def main():
    vector = Vector(x=3, y=1)
    chess_board = ChessBoardBuilder.build(chess_board_id=1)
    squares = chess_board.squares
    coord = chess_board.squares[0][0].coordinate

    square_iterator = SquareIterator(vector=vector, squares=squares, coord=coord)

    while True:
        try:
            square = next(square_iterator)
            print(square)
        except StopIteration:
            break

if __name__ == "__main__":
    main()