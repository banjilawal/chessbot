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
    Raised when a disabled Piece tries to do something..


    # RELATED EXCEPTIONS
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
        "on an initial square cannot act."
    )


class DisabledUnRosteredPieceCannotActException(DisabledPieceException):
    """"""
    ERROR_CODE = "PIECE_NOT_ON_ROSTER_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A Piece must be on its Team roster to act in a scene"


class PieceNotOnBoardCannotActException(TurnSceneException):
    """"""
    ERROR_CODE = "PIECE_NOT_ON_BOARD_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A piece must be on the board to act in a scene,"