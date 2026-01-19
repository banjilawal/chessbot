__all__ = [
    # ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
    "FriendCannotCaptureFriendException",
]

from chess.hostage import HostageManifestException


# ======================# FRIEND_CANNOT_CAPTURE_FRIEND EXCEPTION #======================#
class FriendCannotCaptureFriendException(HostageManifestException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that adding a combatant to the prisoners failed because the token was a friend.

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
    DEFAULT_MESSAGE = "HostageManifest validation failed: A friend cannot be a prisoner."