from typing import List

from chess.factory.emit import id_emitter

from chess.geometry.board.coordinate import Coordinate
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

                square = Square(id_emitter.square_id, name, coordinate)

                row_squares.append(square)
                ascii_value += 1
            grid.append(row_squares)
        return grid


def main():
    from chess.geometry.board import ChessBoard
    board = ChessBoard(grid=GridBuilder.build())
    print(board)





if __name__ == "__main__":
    main()
