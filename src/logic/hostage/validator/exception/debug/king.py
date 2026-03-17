__all__ = [
    # ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
    "KingCannotBeCapturedException",
]

from logic.hostage import HostageException


# ======================# KING_CANNOT_BE_CAPTURED EXCEPTION #======================#
class KingCannotBeCapturedException(HostageException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Indicate that adding a occupant to the prisoners failed because it was a KingToken instead of a CombatantToken

    Super Class:
        *   HostageServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "KING_CANNOT_BE_CAPTURED"
    MSG = "Hostage validation failed: A KingToken cannot be a prisoner"