from typing import List, TYPE_CHECKING

from chess.factory.emit import id_emitter

from chess.geometry.coordinate import Coordinate
from chess.geometry.square import Square
from chess.system_config import ROW_SIZE, COLUMN_SIZE


class GridBuilder:

    @staticmethod
    def build() -> List[List[Square]]:

        grid: List[List[Square]] = []

        for i in range(ROW_SIZE):
            row_squares: List[Square] = []
            ascii_value = ord('A')

            for j in range(COLUMN_SIZE):
                name = chr(ascii_value) + str(i + 1)
                coordinate = Coordinate(row=i, column=j)
                # print("built coord:", coord.name())
                square = Square(id_emitter.square_id, name, coordinate)
                # print("built: square", square.id, "coord:",coord.name() )
                row_squares.append(square)
                ascii_value += 1
            grid.append(row_squares)
        return grid


def main():
    from chess.geometry.board import Board
    board = Board(grid=GridBuilder.build())
    print(board)





if __name__ == "__main__":
    main()
