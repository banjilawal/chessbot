# src/chess/team/prisoner/exception/insertion/friend.py

"""
Module: chess.team.prisoner.exception.insertion.friend
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import HostageServiceException

__all__ = [
    # ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
    "FriendCannotCaptureFriendException",
]


# ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
class FriendCannotCaptureFriendException(HostageServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that adding a combatant to the prisoners failed because the occupant was a friend.

    # PARENT:
        *   HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FRIEND_CANNOT_CAPTURE_FRIEND"
    DEFAULT_MESSAGE = "Adding prisoner failed: A friend cannot be a prisoner."