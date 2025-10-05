# from typing import List
#
# from chess.creator.emit import id_emitter
# from chess.geometry.coord.coord import Coord
# from chess.chessboard.square import Square
# from chess.chessboard.chessboard import ChessBoard
# from chess.system.config import ROW_SIZE, COLUMN_SIZE
#
#
# class ChessBoardBuilder:
#
#   @staticmethod
#   def build() -> ChessBoard:
#
#     squares: List[List[Square]] = []
#
#     for i in range(ROW_SIZE):
#       row_squares: List[Square] = []
#       ascii_value = ord('A')
#
#       for j in range(COLUMN_SIZE):
#         name = chr(ascii_value) + str(i + 1)
#         coord = Coord(row=i, column=j)
#         square = Square(id_emitter.square_id, name, coord)
#         row_squares.append(square)
#         ascii_value += 1
#       squares.append(row_squares)
#     return ChessBoard(board_id=id_emitter.board_id, squares=squares)
#

# def main():
#
#   chess_board = ChessBoardBuilder.build()
#   print(chess_board.__str__())
#
#
#
#
#
# if __name__ == "__main__":
#   main()
