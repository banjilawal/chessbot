# ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
class ResourceUnavailableException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a resource a client needs is unavailable.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RESOURCE_UNAVAILABLE_ERROR"
    DEFAULT_MESSAGE = "Resource is unavailable."
