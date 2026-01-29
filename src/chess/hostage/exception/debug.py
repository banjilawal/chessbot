__all__ = [
    # ======================# HOSTAGE_MANIFEST_DEBUG EXCEPTION #======================#
    "HostageManifestDebugException",
]

from chess.hostage import HostageManifestException
from chess.system import DebugException


# ======================# HOSTAGE_MANIFEST_DEBUG EXCEPTION #======================#
class HostageManifestDebugException(HostageManifestException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused an HostageManifest operation failure.

    # PARENT:
        *   HostageManifestException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_DEBUG_ERROR"
    DEFAULT_MESSAGE = "An hostageManifest debug error occurred."