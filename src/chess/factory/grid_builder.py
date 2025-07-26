from typing import List

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
            row = Row(row_id=i + 1)
            for j in range(COLUMN_SIZE):
                column = Column(column_id=j + 1, name=id_emitter.column_name())
                coordinate = Coordinate(coordinate_id=id_emitter.coordinate_id(), row=row, column=column)
                print(coordinate)
                square = Square(id=id_emitter.square_id(), coordinate=coordinate)
                print(square)
                squares.append(square)
        return squares
