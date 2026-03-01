__all__ = [
    # ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
    "FriendCannotCaptureFriendException",
]

from logic.hostage import HostageException


# ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
class FriendCannotCaptureFriendException(HostageException):
    """
    # ROLE: Exception Wrapper

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
    ERR_CODE = "FRIEND_CANNOT_CAPTURE_FRIEND"
    MSG = "Hostage validation failed: A friend cannot be a prisoner."