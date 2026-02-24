__all__ = [
    # ======================# HOSTAGE_DEBUG EXCEPTION #======================#
    "HostageDebugException",
]

from chess.hostage import HostageException
from chess.system import DebugException


# ======================# HOSTAGE_DEBUG EXCEPTION #======================#
class HostageDebugException(HostageException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused an Hostage operation failure.

    # PARENT:
        *   HostageException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "HOSTAGE_DEBUG_ERROR"
    DEFAULT_MESSAGE = "An hostage debug error occurred."