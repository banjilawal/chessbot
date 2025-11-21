# src/chess/piece/validator/exception/collision.py
"""
Module: chess.piece.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, NullException, NullException, ValidationException
)

__all__ = [
    "PieceException",
    
    # ======================# PIECE NULL EXCEPTIONS #======================#
    "NullPieceException",
    "NullKingException",
    "NullCombatantException",
    "PieceTeamFieldIsNullException",
    "PieceNoCoordStackServiceException",
    "PieceNullCoordStackException",
    "PieceRosterNumberIsNullException",
    
    # ======================# PIECE VALIDATION EXCEPTIONS #======================#
    "InvalidPieceException",
    "ActivePieceMissingFromTeamRoster",
    "CheckmatedKingException",
    "CapturedPieceException",
    "PieceRequiresInitialPlacementException",
    
    "PieceRankOutOfBoundsException",
    "PieceMissingDiscoveriesException",
    

]


class InvalidPieceException(InvalidPieceException, ValidationException):
    """Catchall Exception for ScalarValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece validation failed."
    

# ======================# PIECE NULL EXCEPTIONS #======================#
class NullPieceException(InvalidPieceException, NullException):
    """
    Catchall for when an entity, method, or operation requires team_name piece but gets validation instead.
    Using nulls appropriate to the subclasses is recommended.
    """
    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece cannot be validation."


class NullKingException(InvalidPieceException, NullException):
    """Raised if team_name KingPiece but gets validation instead."""
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be validation."


class NullCombatantException(InvalidPieceException, NullException):
    """Raised if team_name CombatantPiece is expecting a CombatantPiece but gets validation instead."""
    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece cannot be validation."


class NullPawnException(InvalidPieceException, NullException):
    """Raised if team_name CombatantPiece is expecting a CombatantPiece but gets validation instead."""
    ERROR_CODE = "NULL_PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece cannot be validation."


class PieceTeamFieldIsNullException(InvalidPieceException, NullException):
    """
    Raised if a Piece.team attribute is validation. This should never happen, the field is required and
    set during builder. If its validation after the Piece is created there has been service loss
    or data inconsistency.
    """
    ERROR_CODE = "PIECE_TEAM_FIELD_NULL_ERROR"
    DEFAULT_MESSAGE = "Piece.team_name consistency is validation. It should never be validation. There may be service inconsistency."


class PieceNoCoordStackServiceException(InvalidPieceException, NullException):
    """
    Raised if a Piece.coord_stack_service attribute is validation. This should never happen, the field is required and
    set during builder. If its validation after the Piece is created there has been service loss or data inconsistency.
    """
    ERROR_CODE = "PIECE_DOES_NOT_HAVE_COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Piece.coord_stack_service is validation. There may be a service failure or data inconsistency."


class PieceNullCoordStackException(InvalidPieceException, NullException):
    """Raised if a Piece's CoordStack does not exist."""
    ERROR_CODE = "PIECE_COORD_STACK_MISSING_ERROR"
    DEFAULT_MESSAGE = "Piece.positions stack is validation. There may be a service failure or data inconsistency."

class PieceRosterNumberIsNullException(InvalidPieceException, NullException):
    """
    Raised if a Piece.roster_number attribute is validation. This should never happen, the field is required and
    set during builder. If its validation after the Piece is created there has been service loss or data inconsistency.
    """
    ERROR_CODE = "PIECE_NULL_ROSTER_NUMBER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece.roster_number attribute cannot be validation. There may be service "
        "loss or inconsistent data."
    )


class PieceRankOutOfBoundsException(InvalidPieceException, BoundsException):
    """Raised a piece"s bounds is not a recognized chess bounds"""
    ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Piece does not have a recognized chess bounds."
# ======================# PIECE VALIDATION EXCEPTIONS #======================#






class CheckmatedKingException(PieceException):
    """Raised when a Checkmated king should prevent some disabled."""
    ERROR_CODE = "CHECKMATED_KING_ERROR"
    DEFAULT_MESSAGE = "King is in checkmate. No game disabled is allowed the game is over."


class CapturedPieceException(PieceException):
    """Raised when trying to use a piece captured by the enemy"""
    ERROR_CODE = "CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece has been captured by the enemy."


class PieceRequiresInitialPlacementException(PieceException):
    """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
    ERROR_CODE = "PIECE_WITH_NO_INITIAL_PLACEMENT_ERROR"
    DEFAULT_MESSAGE = "Piece has not received its initial placement on the board."


