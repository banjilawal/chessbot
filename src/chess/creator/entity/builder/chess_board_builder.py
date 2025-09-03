from typing import List

from chess.board.board import ChessBoard
from chess.board.square import Square
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.creator.emit import id_emitter
from chess.geometry.coord import Coordinate


class ChessBoardBuilder:


    @staticmethod
    def build(chess_board_id:int) -> ChessBoard:

        squares: List[List[Square]] = []

        for i in range(ROW_SIZE):
            row_squares: List[Square] = []
            ascii_value = ord('A')

            for j in range(COLUMN_SIZE):
                name = chr(ascii_value) + str(i + 1)
                coordinate = Coordinate(row=i, column=j)

                square = Square(id_emitter.square_id, name, coordinate)

                row_squares.append(square)
                ascii_value += 1
            squares.append(row_squares)
        return ChessBoard(board_id=chess_board_id, squares=squares)


def main():
    board = ChessBoardBuilder.build(id_emitter.board_id)
    print(board)

if __name__ == "__main__":
    main()
