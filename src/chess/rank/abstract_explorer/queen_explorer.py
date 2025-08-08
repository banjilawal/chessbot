# from typing import List
#
# from chess.geometry.board.board import ChessBoard
# from chess.geometry.coordinate.coordinate import Coordinate
#
# from chess.team.model.piece import ChessPiece
#
#
# class QueenMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, piece: ChessPiece, board: ChessBoard) -> List[Coordinate]:
#         origin = piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = piece.motion_controller.territories
#         print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         bishop_destinations = BishopMoveGenerator.search(piece, board)
#         castle_destinations = CastleMoveGenerator.search(piece.motion_controller, piece.current_coordinate(), board)
#
#         return bishop_destinations + castle_destinations
