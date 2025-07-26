from typing import List

from chess.common.constant import ROW_SIZE, COLUMN_SIZE
from chess.factory.emit import id_emitter
from chess.geometry.board import Board
from chess.geometry.column import Column
from chess.geometry.coordinate import Coordinate
from chess.geometry.row import Row
from chess.geometry.square import Square

class GridBuilder:

    @staticmethod
    def build() -> List[Square]:
        column_name = id_emitter.column_name
        squares: List[Square] = []

        # columns = []
        # ascii_value = ord('A')
        # for i in range(COLUMN_SIZE):  # Only 8 columns: A to H
        #     print(i, chr(ascii_value))
        #     column_name = chr(ascii_value)
        #     column = Column(i + 1, column_name)
        #     columns.append(column)
        #     print(column.name + "-"+ str(column.id))
        #     ascii_value += 1
        #
        # rows = []
        # for i in range(ROW_SIZE):
        #     row = Row(i + 1)
        #     rows.append(row)
        #     # column = Column(i + 1, id_emitter.column_name)
        #     # print(i,  column.name)
        #     # columns.append(column)

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
    board = Board()
    print(board.squares)




if __name__ == "__main__":
    main()
