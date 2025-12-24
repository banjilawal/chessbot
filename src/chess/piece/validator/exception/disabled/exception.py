# src/chess/piece/validator/exception/disabled/collision.py

"""
Module: chess.piece.validator.exception.disabled.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.piece import InvalidPieceException


class DisabledPieceException(InvalidPieceException):
    """
    # RESPONSIBILITY
    Raised when a disabled Piece tries to do something.


    # RELATED EXCEPTION
        *   AttackException
        *   CastlingException
        *   CheckmateException
        *   HostageException
        *   NullException
        *   PromotionException
        *   RosterException
        *   TravelException
    """

class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )


class PieceRequiresInitialPlacementException(PieceException):
    """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
    ERROR_CODE = "PIECE_WITH_NO_INITIAL_PLACEMENT_ERROR"
    DEFAULT_MESSAGE = "Piece has not received its initial placement on the board."


class DisabledHostagePieceException(DisabledPieceException):
    """"""
    ERROR_CODE = "CAPTURED_PIECE_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot act in a scene."



class PieceWithNoStartingPlacementException(TurnSceneException):
    """Raised when team_name potential actor_candidate has not been placed on the board_validator."""
    ERROR_CODE = "PIECE_WITH_NO_INITIAL_PLACEMENT_ERROR"
    DEFAULT_MESSAGE = (
        "A Piece never placed at its starting position cannot act in a scene. A piece never placed "
        "on an initial square_name cannot act."
    )






class HostageActivityException(PieceException):
    """
    Several exception can be raised during capture rollback. This class is the parent of
    exception an attacking owner can raised. Do not use directly. Subclasses give details
    useful for debugging.
    """
    ERROR_CODE = "HOSTAGE_ACTIVITY_ERROR"
    DEFAULT_MESSAGE = "Hostage owner cannot move, blocking, or attack."


class HostageCannotAttackException(HostageActivityException):
    """
    Raised if team_name captured owner tries to attack.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
    DEFAULT_MESSAGE = "Captured owner cannot attack."


class HostageCannotMoveException(HostageActivityException):
    """
    Raised if team_name captured owner tries to move.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_MOVE_ERROR"
    DEFAULT_MESSAGE = "Captured owner cannot move."


class HostageCannotScanException(HostageActivityException):
    """
    Raised if team_name captured owner tries to blocking team_name square_name.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
    DEFAULT_MESSAGE = "Captured owner cannot blocking team_name sqaure."


