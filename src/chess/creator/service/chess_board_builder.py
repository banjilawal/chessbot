from typing import List

from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import Coordinate
from chess.board.element.square import Square
from chess.board.board import ChessBoard
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.board.map_service import MapService


class ChessBoardBuilder:

    @staticmethod
    def assemble():
        return MapService(repo=ChessBoardBuilder._build_repo(), )

    @staticmethod
    def _build_repo() -> ChessBoard:

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
        return ChessBoard(grid)

#
#
#
# def main():
#
#     service = ChessBoardBuilder.assemble()
#     print(service.squares_to_string())
#
#
#
#
#
# if __name__ == "__main__":
#     main()
