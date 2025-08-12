from typing import Optional

from assurance.validation.chess_piece_specification import ChessPieceSpecification
from assurance.validation.coordinate_specification import CoordinateSpecification
from assurance.validation.validation_exception import ChessPieceValidationException, CoordinateValidationException
from chess.board.board import ChessBoard
from chess.exception.null_exception import NullChessBoardExcepton
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.geometry.line.vertical import Vertical

from chess.walk.walk import Walk, DestinationUnreachableException
from chess.token.chess_piece import ChessPiece

class PawnWalkException(DestinationUnreachableException):
    default_message = f"{DestinationUnreachableException.default_message}"

class PawnAdvanceException(PawnWalkException):
    default_message = f"{PawnWalkException.default_message} by advancing pawn"

class PawnAttackException(PawnWalkException):
    default_message = f"{PawnWalkException.default_message} for a pawn attack"

class UnsatisfiedPawnWalkPreConditionException(PawnWalkException):
    default_message = f"Preconditions for PawnWalk destination evaluation not met"

class PawnWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holing PawnRank
    """

    @staticmethod
    def is_walkable(
        chess_piece: ChessPiece,
        destination: Coordinate,
        chess_board: Optional[ChessBoard] = None
    ) -> bool:
        method="PawnWalk.is_walkable"

        """
            Implementation of Walk for a Pawn. Uses helper methods for handling use case
            - Pawn advancing
            - Pawn attacking
        """

        if chess_board is None:
            raise NullChessBoardExcepton(f"{method} {NullChessBoardExcepton.default_message}")

        origin = chess_piece.coordinate_stack.current_coordinate()

        row_diff = destination.row - origin.row
        column_diff = abs(destination.column - origin.column)

        black_pawn_attack_squares = [
            chess_board.find_square_by_coordinate(Coordinate(origin.row + 1, origin.column - 1)),
            chess_board.find_square_by_coordinate(Coordinate(origin.row + 1, origin.column + 1))
        ]

        white_pawn_attack_squares = [
            chess_board.find_square_by_coordinate(Coordinate(origin.row - 1, origin.column - 1)),
            chess_board.find_square_by_coordinate(Coordinate(origin.row - 1, origin.column + 1))
        ]

        if column_diff > 1:
            raise PawnWalkException(
                f"{method} {chess_piece.name} cannot walk to {destination} "
                f"the destination is more than one column away from origin {origin}"
            )
        if abs(row_diff) > 2:
            raise PawnWalkException(
                f"{method} {chess_piece.name} cannot walk to {destination} "
                f"the destination is more than two rows away from origin {origin}"
            )
        if row_diff == 2 and chess_piece.coordinate_stack.size() > 1:
            raise PawnWalkException(
                f"{method} {chess_piece.name} cannot walk to {destination} "
                f"the destination is two rows away from origin {origin} "
                f"but the pawn has already moved"
            )
        if (row_diff == 1 and column_diff == 1 and
                chess_piece.team.color == "BLACK" and
                destination not in black_pawn_attack_coords):

            raise PawnWalkException(
                f"{method} {chess_piece.name} cannot walk to {destination} "
                f"the destination is one row and one column away from origin {origin} "
                f"this is not a legal pawn attack"
            )
        quadrant = chess_piece.team.home_quadrant
        delta = quadrant.delta
        print(f"Pawn {chess_piece.name} quadrant:")
        return (
            PawnWalk.can_advance(chess_piece, destination) or
            PawnWalk.can_attack(chess_piece, destination)
        )



    @staticmethod
    def can_advance(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        method="PawnWalk.can_advance"

        """
        Helper method for PawnWalk.is_walkable. Handles case of advancing pawn.
        
        Args:
            chess_piece (ChessPiece): row index
            destination (Coordinate): column index
            
        Returns:
            True if the destination can be reach by a legal pawn advance movement

        Raise:
            NullChessPieceException: If chess_piece is null.
            NullCoordinateException: If destination is null.
            CoordinateException: If destination properties are invalid.       
        """

        if not PawnWalk._satisfies_walk_preconditions(chess_piece, destination):
            raise UnsatisfiedPawnWalkPreConditionException(
                UnsatisfiedPawnWalkPreConditionException.default_message
            )
            # print(f"{chess_piece.name} does not satisfy walk preconditions to advance")
            # return False
        #
        # if PawnWalk._number_of_advancing_steps(chess_piece, destination) == 0:
        #     print(f"{chess_piece.name} cannot advance to {destination}")
        #     return False
        return True


    @staticmethod
    def can_attack(pawn: ChessPiece, destination: Coordinate) -> bool:
        method = "PawnWalk.can_attack"

        """
        Helper method for PawnWalk.is_walkable. Handles case of attacking pawn.
        
        Args:
            chess_piece (ChessPiece): row index
            destination (Coordinate): column index
            
        Returns:
            True if the destination can be reach by a legal pawn attack movement

        Raise:
            NullChessPieceException: If chess_piece is null.
            NullCoordinateException: If destination is null.
            CoordinateException: If destination properties are invalid.  
        """

        if not PawnWalk._satisfies_walk_preconditions(pawn, destination):
            print(f"{pawn.name} does not satisfy walk preconditions to advance")
            return False

        origin = pawn.coordinate_stack.current_coordinate()

        # Must be diagonal (NOT vertical for attacks)
        if not Diagonal.is_diagonal(origin, destination):
            raise PawnAttackException(
                f"{method} "
                f"{pawn.name} origin {origin} "
                f"cannot attack {destination} "
                f"the destination is more one row away from origin"
                f"{method} returning False"
            )

        if abs(destination.column - origin.column) != 1:
            raise PawnAttackException(
                f"{method} "
                f"{pawn.name} origin {origin} "
                f"cannot attack {destination} "
                f"the destination is more than one column away from origin"
                f"{method} returning False"
            )

        row_diff = destination.row - origin.row
        from chess.config.team_config import TeamConfig
        expected_direction = -1 if pawn.team.config == TeamConfig.WHITE else 1
        return True


    @staticmethod
    def _satisfies_walk_preconditions(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        method = f"PawnWalk._satisfies_walk_preconditions"

        """
        Helper that centralizes validation public methods PawnWalk

        Args:
            chess_piece (ChessPiece): row index
            destination (Coordinate): column index

        Returns:
            True if the destination can be reach by a legal pawn attack movement

        Raise:
            NullChessPieceException: If chess_piece is null.
            NullCoordinateException: If destination is null.
            UnplacedChessPieceMoveException: If chess_piece is not on the board. 
            UnsatisfiedPawnWalkPreConditionException: If there is no vertical relationship between
                pawn and destination.
        """

        if not CoordinateSpecification.is_satisfied_by(destination):
            raise CoordinateValidationException(
                f"{method} {CoordinateValidationException.default_message}"
            )

        if not ChessPieceSpecification.is_satisfied_by(chess_piece):
            raise ChessPieceValidationException(
                f"{method} {ChessPieceValidationException.default_message}"
            )
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
