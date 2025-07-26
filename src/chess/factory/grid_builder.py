from typing import List, TYPE_CHECKING

from chess.common.constant import ROW_SIZE, COLUMN_SIZE
from chess.factory.emit import id_emitter

from chess.geometry.column import Column
from chess.geometry.coordinate import Coordinate
from chess.geometry.row import Row
from chess.geometry.square import Square





class GridBuilder:

    @staticmethod
    def build() -> List[Square]:

        squares: List[Square] = []

        for i in range(ROW_SIZE):
            row = Row(row_id=(i + 1))
            ascii_value = ord('A')

            for j in range(COLUMN_SIZE):
                column = Column(j + 1, chr(ascii_value))
                coordinate = Coordinate(coordinate_id=id_emitter.coordinate_id, row=row, column=column)
                # print("built coord:", coordinate.name())
                square = Square(id_emitter.square_id, coordinate)
                print("built: square", square.id, "coord:",coordinate.name() )
                squares.append(square)
                ascii_value += 1
        return squares


def main():
    from chess.geometry.board import Board
    board = Board()
    print(board.grid)




if __name__ == "__main__":
    main()
