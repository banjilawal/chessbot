__all__ = [
    # ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
    "FriendCannotCaptureFriendException",
]

from model.hostage import HostageException


# ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
class FriendCannotCaptureFriendException(HostageException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that adding a combatant to the prisoners failed because the occupant was a friend.

    Super Class:
        *   HostageServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FRIEND_CANNOT_CAPTURE_FRIEND"
    MSG = "Hostage validation failed: A friend cannot be a prisoner."