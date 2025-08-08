# from typing import List
#
# from chess.geometry.obsolete_board.obsolete_board import ObsoleteChessBoard
# from chess.geometry.coordinate.coordinate import Coordinate
#
# from chess.team.element.chess_piece import ChessPiece
#
#
# class QueenMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, chess_piece: ChessPiece, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = chess_piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = chess_piece.rank.territories
#         print(f"{chess_piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         bishop_destinations = BishopMoveGenerator.search(chess_piece, obsolete_board)
#         castle_destinations = CastleMoveGenerator.search(chess_piece.rank, chess_piece.current_coordinate(), obsolete_board)
#
#         return bishop_destinations + castle_destinations
