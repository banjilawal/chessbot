# src/chess/player/model/exception.py

"""
Module: chess.player.model.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# PLAYER EXCEPTION #======================#
    "PlayerException",
]


# ======================# PLAYER EXCEPTION #======================#
class PlayerException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Player errors not covered by PlayerException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_ERROR"
    MSG = "Player raised an exception."
#
# #======================# PLAYER_HISTORY EXCEPTION #======================#
# class PlayerPlayerHistoryException(PlayerPlayerException):
#   """Team list specific errors."""
#   ERR_CODE = "PLAYERPLAYER_HISTORY_ERROR"
#   MSG = "PlayerPlayerHistory raised an exception."
#
# class InconsistentCommandHistoryException(PlayerPlayerHistoryException, InconsistentCollectionException):
#   ERR_CODE = "INCONSISTENT_PLAYERPLAYER_HISTORY_ERROR"
#   MSG = (
#     "PlayerPlayerHistory is an inconsistent state. Data might be corrupt."
#   )
#
# class PushNewTeamException(PlayerPlayerHistoryException):
#   """Raised if team_name new team_name could not be pushed to commandHistory"""
#   ERR_CODE = "PUSH_NEW_TEAM_ERROR"
#   MSG = "Could not push team_name new team_name to TeamStack."
#
# class UndoingPushTeamFailedException(PlayerPlayerHistoryException):
#   """Raised if removing the updated team_name failed"""
#   ERR_CODE = "UNDOING_PUSH_TEAM_FAILED_ERROR"
#   MSG = "Could not undo the new team_name addition."
#
# class CannotRemoveOldTeamException(PlayerPlayerHistoryException):
#   """Raised if an attempt is made to remove an old team_name from TeamStack"""
#   ERR_CODE = "REMOVE_OLD_TEAM_ERROR"
#   MSG = "Removing old team_service from TeamStack is not allowed."
#
# class InvalidPlayerPlayerAssignmentException(PlayerPlayerHistoryException):
#   """
#   If team_name team_name already attached to team_name owner (team_name.owner == not None) tries being assigned team_name
#   different owner, `InvalidPlayerPlayerAssignmentException` is raised.
#   """
#   ERR_CODE = "INVALID_PLAYERPLAYER_ASSIGNMENT_ERROR"
#   MSG = "Team is already assigned to team_name different owner."




