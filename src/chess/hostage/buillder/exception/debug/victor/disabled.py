from chess.hostage import HostageManifestException
from chess.system import DebugException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_BUILD_FAILURE EXCEPTION #======================#
    "VictorCannotBeDisableTokenException",
]


# ======================# VICTOR_CANNOT_BE_DISABLED_TOKEN EXCEPTION #======================#

class VictorCannotBeDisableTokenException(HostageManifestException, DebugException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that the HostageManifest build failed because the victor was not active for the build process.
        A token must be active when it creates a capture event.

    # PARENT:
        *   DebugException
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VICTOR_CANNOT_BE_DISABLED_TOKEN_ERROR"
    DEFAULT_MESSAGE = "HostageManifest build failed: Victor cannot be disabled. It must be active during the build."