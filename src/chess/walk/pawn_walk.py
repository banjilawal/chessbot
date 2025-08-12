# from chess.token.chess_piece import ChessPiece
#
#
# class PawnWalk(Walk):
#     @staticmethod
#     def is_walkable(chess_piece: ChessPiece, destination: Coordinate, chess_board: Optional[ChessBoard] = None) -> bool:
#         if not chess_piece or not destination:
#             return False
#
#         origin = chess_piece.coordinate_stack.current_coordinate()
#         if not origin:
#             return False
#
#         direction = 1 if chess_piece.team.name == "BLACK" else -1
#         row_diff = destination.row - origin.row
#         col_diff = abs(destination.column - origin.column)
#
#         # Forward move
#         if col_diff == 0:
#             if row_diff == direction:
#                 return chess_board.is_empty(destination)
#             elif row_diff == 2 * direction and PawnWalk._is_on_starting_row(chess_piece):
#                 intermediate = Coordinate(origin.row + direction, origin.column)
#                 return chess_board.is_empty(intermediate) and chess_board.is_empty(destination)
#             return False
#
#         # Diagonal attack
#         elif col_diff == 1 and row_diff == direction:
#             return chess_board.has_opponent_piece(chess_piece.team, destination)
#
#         return False
#
#     @staticmethod
#     def _is_on_starting_row(chess_piece: ChessPiece) -> bool:
#         return (
#             (chess_piece.team.name == "WHITE" and chess_piece.coordinate_stack.current_coordinate().row == 6) or
#             (chess_piece.team.name == "BLACK" and chess_piece.coordinate_stack.current_coordinate().row == 1)
#         )
