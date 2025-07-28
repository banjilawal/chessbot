# from typing import List
#
# from chess.geometry.board import Board
# from chess.piece.piece import Piece
# from chess.motion.walk import Walk
#
#
# class ExploratorySearch:
#
#     @staticmethod
#     def exploratory(piece: Piece, board: Board) -> List[Coordinate]:
#         if not piece or not board or not piece.current_position():
#             return []
#
#         origin = piece.current_position()
#         destinations = []
#
#         if isinstance(piece, Knight):
#             for dest in Walk.knight_walk(origin):
#                 if not board.coordinate_is_valid(dest):
#                     continue
#                 occupant = board.get_chess_piece_by_coordinate(dest)
#                 if occupant is None or piece.is_enemy(occupant):
#                     destinations.append(dest)
#
#         elif isinstance(piece, King):
#             for dest in Walk.king_walk(origin):
#                 if not board.coordinate_is_valid(dest):
#                     continue
#                 occupant = board.get_chess_piece_by_coordinate(dest)
#                 if occupant is None or piece.is_enemy(occupant):
#                     destinations.append(dest)
#
#         elif isinstance(piece, Pawn):
#             team_home = piece.team.home
#             # Forward move (1 square ahead unless blocked)
#             delta = Quadrant.N.delta if team_home.is_north else Quadrant.S.delta
#             forward = origin.shift(Delta(*delta))
#             if board.coordinate_is_valid(forward) and not board.get_chess_piece_by_coordinate(forward):
#                 destinations.append(forward)
#
#             # Diagonal attacks
#             diagonals = [Quadrant.NE, Quadrant.NW] if team_home.is_north else [Quadrant.SE, Quadrant.SW]
#             for q in diagonals:
#                 dest = origin.shift(Delta(q.x_delta, q.y_delta))
#                 if board.coordinate_is_valid(dest):
#                     occupant = board.get_chess_piece_by_coordinate(dest)
#                     if occupant and piece.is_enemy(occupant):
#                         destinations.append(dest)
#
#         else:
#             # Rook, Bishop, Queen, etc.
#             walk_method = Walk.bishop_walk if piece.rank.is_bishop() else \
#                           Walk.castle_walk if piece.rank.is_rook() else \
#                           Walk.queen_walk if piece.rank.is_queen() else None
#
#             if not walk_method:
#                 return []
#
#             quadrants = []
#             if walk_method == Walk.bishop_walk:
#                 quadrants = [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW]
#             elif walk_method == Walk.castle_walk:
#                 quadrants = [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W]
#             elif walk_method == Walk.queen_walk:
#                 quadrants = [q for q in Quadrant]
#
#             for q in quadrants:
#                 step = 1
#                 while True:
#                     delta = Delta(q.x_delta * step, q.y_delta * step)
#                     dest = origin.shift(delta)
#                     if not board.coordinate_is_valid(dest):
#                         break
#                     occupant = board.get_chess_piece_by_coordinate(dest)
#                     if occupant is None:
#                         destinations.append(dest)
#                     elif piece.is_enemy(occupant):
#                         destinations.append(dest)
#                         break
#                     else:
#                         break
#                     step += 1
#
#         return destinations