from typing import TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.geometry.line.vertical import Vertical

from chess.walk.walk import Walk
from chess.token.chess_piece import ChessPiece



class PawnWalk(Walk):
    """
    Consolidated captor movement validation with specialized static methods
    for different movement types.
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        """
        Basic geometric reachability - maintains Walk interface.
        Only checks if destination is geometrically walk by captor movement.
        """
        return (
            PawnWalk.can_advance(chess_piece, destination) or
            PawnWalk.can_attack(chess_piece, destination)
        )


    @staticmethod
    def can_advance(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        if not PawnWalk._satisfies_walk_preconditions(chess_piece, destination):
            print(f"{chess_piece.name} does not satisfy walk preconditions to advance")
            return False
        if PawnWalk._number_of_advancing_steps(chess_piece, destination) == 0:
            print(f"{chess_piece.name} cannot advance to {destination}")
            return False
        return True


    @staticmethod
    def can_attack(pawn: ChessPiece, destination: Coordinate) -> bool:
        method = "PawnWalk.can_attack"

        if not PawnWalk._satisfies_walk_preconditions(pawn, destination):
            print(f"{pawn.name} does not satisfy walk preconditions to advance")
            return False

        origin = pawn.coordinate_stack.current_coordinate()

        # Must be diagonal (NOT vertical for attacks)
        if not Diagonal.is_diagonal(origin, destination):
            raise ValueError(
                f"{method} "
                f"{pawn.name} origin {origin} "
                f"is not diagonal from {destination} "
                f" cannot attack"
            )

        if abs(destination.column - origin.column) != 1:
            raise ValueError(
                f"{method} "
                f"{pawn.name} origin {origin} "
                f"s not one column away from attack coordinate {destination}"
            )

        row_diff = destination.row - origin.row
        from chess.config.team_config import TeamConfig
        expected_direction = -1 if pawn.team.config == TeamConfig.WHITE else 1
        return True


    @staticmethod
    def _satisfies_walk_preconditions(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        method = f"PawnWalk._satisfies_walk_preconditions"

        if chess_piece is None:
            raise ValueError(f"{method} ChessPiece cannot be None in precond check")
        if destination is None:
            raise ValueError(f"{method} Destination cannot be None in precond check")

        from chess.rank.promotable.pawn_rank import PawnRank
        if not isinstance(chess_piece.rank, PawnRank):
            raise ValueError(f"{method} ChessPiece rank is not a PawnRank")

        pawn = chess_piece

        if pawn.coordinate_stack is None:
            raise ValueError(
                f"{method} "
                f"Pawn {pawn.name} has no coordinate_stack cannot advance"
            )

        if pawn.coordinate_stack.current_coordinate() is None or pawn.coordinate_stack.size() == 0:
            raise ValueError(
                f"{method} "
                f"Pawn {pawn.name} "
                f"has stack size {pawn.coordinate_stack.size()} "
                f" {pawn.name} is not on the chess board cannot advance"
            )

        if not Vertical.is_vertical(pawn.coordinate_stack.current_coordinate(), destination):
            raise ValueError(f"{method} Pawn {pawn.name} cannot advance to non-vertical destination")

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
