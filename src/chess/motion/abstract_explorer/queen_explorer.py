# from typing import List
#
# from chess.geometry.obsolete_board.obsolete_board import ObsoleteChessBoard
# from chess.geometry.coordinate.coordinate import Coordinate
#
# from chess.team.element.piece import ChessPiece
#
#
# class QueenMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, piece: ChessPiece, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = piece.rank.territories
#         print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         bishop_destinations = BishopMoveGenerator.search(piece, obsolete_board)
#         castle_destinations = CastleMoveGenerator.search(piece.rank, piece.current_coordinate(), obsolete_board)
#
#         return bishop_destinations + castle_destinations
