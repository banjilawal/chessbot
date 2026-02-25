__all__ = [
    # ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
    "KingCannotBeCapturedException",
]

from chess.hostage import HostageException


# ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
class KingCannotBeCapturedException(HostageException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that adding a occupant to the prisoners failed because it was a KingToken instead of a CombatantToken

    # PARENT:
        *   HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "KING_CANNOT_BE_CAPTURED"
    MSG = "Hostage validation failed: A KingToken cannot be a prisoner"