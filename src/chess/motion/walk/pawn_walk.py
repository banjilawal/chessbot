from typing import Optional

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.geometry.line.vertical import Vertical
from chess.map.element.occupation_status import OccupationStatus
from chess.map.map_service import MapService
from chess.motion.walk.walk import Walk
from chess.team.model.piece import ChessPiece
from chess.motion.controller.pawn_motion_controller import PawnMotionController


class PawnWalk(Walk):
    """
    Consolidated chess_piece movement validation with specialized static methods
    for different movement types.
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate, map_service: MapService) -> Optional[bool]:
        """
        Basic geometric reachability - maintains Walk interface.
        Only checks if destination is geometrically walk by chess_piece movement.
        """
        return (PawnWalk.can_advance(chess_piece=chess_piece, destination=destination) or
            PawnWalk.can_attack(
                pawn=chess_piece,
                destination=destination,
                map_service=map_service
            )
        )


    @staticmethod
    def can_advance(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        if not PawnWalk._satisfies_walk_preconditions(chess_piece):
            print(f"{chess_piece.name} does not satisfy walk preconditions to advance")
            return False
        if PawnWalk._number_of_advancing_steps(chess_piece, destination) == 0:
            print(f"{chess_piece.name} cannot advance to {destination}")
            return False
        return True


    @staticmethod
    def can_attack(pawn: ChessPiece, destination: Coordinate, map_service: MapService) -> bool:
        if not PawnWalk._satisfies_walk_preconditions(pawn):
            print(f"{pawn.name} does not satisfy walk preconditions to advance")
            return False

        if Diagonal.is_diagonal(pawn.coordinate_stack.current_coordinate(), destination):
            print(f"{pawn.name} is not diagonal from attack coordinate {destination}")
            return False

        if abs(destination.column - pawn.coordinate_stack.current_coordinate().column) != 1:
            print(f"{pawn.name} is not one column away from attack coordinate {destination}")
            return False

        if map_service.find_square_by_coordinate(destination).status != OccupationStatus.HAS_ENEMY:
            return False
        return True


    @staticmethod
    def _satisfies_walk_preconditions(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        if chess_piece is None:
            print("Pawn is None cannot advance")
            return False
        if not isinstance(chess_piece.motion_controller, PawnMotionController):
            print("ChessPiece is not a chess_piece cannot advance")
            return False

        pawn = chess_piece

        if pawn.coordinate_stack is None:
            print("Pawn has no coordinate_stack cannot advance")
            return False
        if pawn.coordinate_stack.current_coordinate() is None or pawn.coordinate_stack.size() == 0:
            print("Pawn is not on the board cannot advance")
            return False
        if not Vertical.is_vertical(pawn.coordinate_stack.current_coordinate(), destination):
            print("Pawn cannot advance to non-vertical destination")
            return False
        return True


    @staticmethod
    def _number_of_advancing_steps(pawn: ChessPiece, destination: Coordinate) -> int:
        row_diff = destination.row - pawn.coordinate_stack.current_coordinate().row
        if row_diff < 0:
            return 0

        if pawn.coordinate_stack.size() == 1:
            return 2
        if pawn.coordinate_stack.size() > 1:
            return  1
        return 0
