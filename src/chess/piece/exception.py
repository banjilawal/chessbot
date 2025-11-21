# src/chess/piece/collision.py

"""
Module: chess.piece.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
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

# ======================# PIECE BUILD EXCEPTIONS #======================#
    "PieceBuildFailedException",
]


class PieceException(ChessException):
    """
    Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an rollback_exception."
    
# ======================# PIECE NULL EXCEPTIONS #======================#
class NullPieceException(PieceException, NullException):
    """
    Catchall for when an entity, method, or operation requires team_name piece but gets null instead.
    Using nulls appropriate to the subclasses is recommended.
    """
    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece cannot be null."


class NullKingException(NullPieceException):
    """Raised if team_name KingPiece but gets null instead."""
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be null."


class NullCombatantException(NullPieceException):
    """Raised if team_name CombatantPiece is expecting a CombatantPiece but gets null instead."""
    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece cannot be null."


class NullPawnException(NullPieceException):
    """Raised if team_name CombatantPiece is expecting a CombatantPiece but gets null instead."""
    ERROR_CODE = "NULL_PAWN_PIECE_ERROR"
    DEFAULT_MESSAGE = "PawnPiece cannot be null."
    
class PieceTeamFieldIsNullException(PieceException, InconsistencyException):
    """
    Raised if a Piece.team attribute is null. This should never happen, the field is required and
    set during builder. If its null after the Piece is created there has been service loss
    or data inconsistency.
    """
    ERROR_CODE = "PIECE_TEAM_FIELD_NULL_ERROR"
    DEFAULT_MESSAGE = "Piece.team_name consistency is null. It should never be null. There may be service inconsistency."


class PieceNoCoordStackServiceException(PieceException, InconsistencyException):
    """
    Raised if a Piece.coord_stack_service attribute is null. This should never happen, the field is required and
    set during builder. If its null after the Piece is created there has been service loss or data inconsistency.
    """
    ERROR_CODE = "PIECE_DOES_NOT_HAVE_COORD_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Piece.coord_stack_service is null. There may be a service failure or data inconsistency."


class PieceNullCoordStackException(PieceException, InconsistencyException):
    """Raised if a Piece's CoordStack does not exist."""
    ERROR_CODE = "PIECE_COORD_STACK_MISSING_ERROR"
    DEFAULT_MESSAGE = "Piece.positions stack is null. There may be a service failure or data inconsistency."


class PieceMissingDiscoveriesException(PieceException, InconsistencyException):
    """
    Raised if piece.discovery list does not exist. If the piece.discoveries == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "PIECE_DISCOVERY_LIST_MISSING_ERROR"
    DEFAULT_MESSAGE = "Piece.discovery list is null. It should never be null. There may be service inconsistency or loss."


class PieceRosterNumberIsNullException(PieceException, NullException):
    """
    Raised if a Piece.roster_number attribute is null. This should never happen, the field is required and
    set during builder. If its null after the Piece is created there has been service loss or data inconsistency.
    """
    ERROR_CODE = "PIECE_NULL_ROSTER_NUMBER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece.roster_number attribute cannot be null. There may be service "
        "loss or inconsistent data."
    )

    
    
# ======================# PIECE VALIDATION EXCEPTIONS #======================#
class InvalidPieceException(PieceException, ValidationException):
    """Catchall Exception for ScalarValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece validation failed."


class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )


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


class PieceRankOutOfBoundsException(PieceException, NullException):
    """Raised a piece"s bounds is not a recognized chess bounds"""
    ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Piece does not have a recognized chess bounds."




