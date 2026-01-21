from chess.system import ServiceException


__all__ = [
    # ======================# HASH_SERVICE EXCEPTION #======================#
    "HashServiceException",
]


# ======================# HASH_SERVICE EXCEPTION #======================#
class HashServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Basic, Service Primitive

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HASH_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HashService raised an exception."