# src/chess/system/resolution/failure/id/exception.py

"""
Module: chess.system.resolution.failure.id.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.system.resolution import ResolutionException

__all__ = [
    "ResolvingIDConflictFailedException",
    "ResolvingSquareIDConflictFailedException",
    "ResolvingPieceIDConflictFailedException",
    "ResolvingTeamIDConflictFailedException",
    "ResolvingAgentIDConflictFailedException",
    "ResolvingBoardIDConflictFailedException"
]


class ResolvingIDConflictFailedException(ResolutionException):
    """
    # RESPONSIBILITY
    Raised when searching with a globally unique attribute like an id and
    the resolution process shows the entity is a orphan


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
    ERROR_CODE = "RESOLUTION_FAILED_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the attribute conflict."


class ResolvingSquareIDConflictFailedException(ResolvingIDConflictFailedException):
    DEFAULT_CODE = "SQUARE_ID_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Square.id conflict."


class ResolvingPieceIDConflictFailedException(ResolvingIDConflictFailedException):
    DEFAULT_CODE = "PIECE_ID_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Token.id conflict."


class ResolvingTeamIDConflictFailedException(ResolvingIDConflictFailedException):
    DEFAULT_CODE = "TEAM_ID_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Team.id conflict."


class ResolvingAgentIDConflictFailedException(ResolvingIDConflictFailedException):
    DEFAULT_CODE = "AGENT_ID_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the PlayerAgent.id conflict."


class ResolvingBoardIDConflictFailedException(ResolvingIDConflictFailedException):
    DEFAULT_CODE = "BOARD_ID_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Board.id conflict."
    
    
