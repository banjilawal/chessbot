from typing import List

from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import Coordinate
from chess.square.model.square import Square
from chess.square.repo.square_repo import SquareRepo
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.square.service.square_service import SquareService


class SquareServiceBuilder:

    @staticmethod
    def assemble():
        return SquareService(repo=SquareServiceBuilder._build_repo(), )

    @staticmethod
    def _build_repo() -> SquareRepo:

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
        return SquareRepo(grid)




def main():

    service = SquareServiceBuilder.assemble_service()
    print(service.square_repo)





if __name__ == "__main__":
    main()
