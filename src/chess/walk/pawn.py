from chess.geometry.coordinate.coord import Coordinate
from chess.geometry.vector.delta import Offset


from chess.walk.base import Walk
from chess.token.model import ChessPiece



class PawnWalk(Walk):
    """
    Consolidated chess_piece movement validation with specialized static methods
    for different movement types.
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        """
        Basic geometric reachability - maintains Walk interface.
        Only checks if destination is geometrically walk by chess_piece movement.
        """
        return (
            PawnWalk.can_advance(chess_piece, destination) or
            PawnWalk.can_attack(chess_piece, destination)
        )


    @staticmethod
    def can_advance(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        origin = chess_piece.positions.current_coordinate()
        forward_step = chess_piece.team.home_quadrant.forward_step
        print(f"quadrant for "
              f"\n{chess_piece.name} "
              f"\non team {chess_piece.team} is "
              f"\n{chess_piece.team.home_quadrant}"
          )
        row_diff = destination.row - origin.row
        column_diff  = destination.column - origin.column
        print(f"Expecting 2 for row_diff got {row_diff} on forward stop {forward_step}")
        print(f"Expecting 0 for column_diff got {column_diff} on forward stop {forward_step}")

        # Allow 2-step move only on first move
        if chess_piece.positions.size() == 1 and row_diff == 2 * forward_step:
            return True

        return row_diff == forward_step and origin.column == destination.column

    @staticmethod
    def can_attack(pawn: ChessPiece, destination: Coordinate) -> bool:
        origin = pawn.positions.current_coordinate()
        delta = Offset(
            delta_column=destination.column - origin.column,
            row_offset=destination.row - origin.row
        )

        return any(delta == q.delta for q in pawn.rank.territories)

