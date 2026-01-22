# from typing import List
#
# from chess.creator.emit import id_emitter
# from chess.geometry.point.point import Coord
# from chess.chessboard.square_name import Square
# from chess.chessboard.chessboard import ChessBoard
# from chess.system.config import NUMBER_OF_ROWS, NUMBER_OF_COLUMNS
#
#
# class ChessBoardBuilder:
#
#   @staticmethod
#   def builder() -> ChessBoard:
#
#     squares: List[List[Square]] = []
#
#     for i in range(NUMBER_OF_ROWS):
#       row_squares: List[Square] = []
#       ascii_value = ord('A')
#
#       for j in range(NUMBER_OF_COLUMNS):
#         visitor_name = chr(ascii_value) + str(i + 1)
#         point = Coord(row=i, column=j)
#         square_name = Square(id_emitter.visitor_id, visitor_name, point)
#         row_squares.append(square_name)
#         ascii_value += 1
#       squares.append(row_squares)
#     return ChessBoard(board_id=id_emitter.board_id, squares=squares)
#

# def main():
#
#   chess_board = ChessBoardBuilder.builder()
#   print(chess_board.__str__())
#
#
#
#
#
# if __name__ == "__main__":
#   main()
