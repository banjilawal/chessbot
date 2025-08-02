from typing import List

from chess.factory.emit import id_emitter

from chess.geometry.coordinate.coordinate import Coordinate
from chess.square.model.square import Square
from chess.square.repo.square_repo import SquareRepo
from chess.system_config import ROW_SIZE, COLUMN_SIZE


class SquareRepoBuilder:

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

    repo = SquareRepo(squares=SquareRepoBuilder.build())
    print(repo)





if __name__ == "__main__":
    main()
