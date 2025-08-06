from typing import List

from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import Coordinate
from chess.grid.model.square import Square
from chess.grid.repo.grid_repo import GridRepo
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.grid.service.grid_service import GridService


class SquareServiceBuilder:

    @staticmethod
    def assemble():
        return GridService(repo=SquareServiceBuilder._build_repo(), )

    @staticmethod
    def _build_repo() -> GridRepo:

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
        return GridRepo(grid)

#
#
#
# def main():
#
#     service = SquareServiceBuilder.assemble()
#     print(service.squares_to_string())
#
#
#
#
#
# if __name__ == "__main__":
#     main()
