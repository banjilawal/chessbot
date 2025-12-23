from chess.system import HashServiceException, ServiceException

__all__ = [
    # ======================# META_HASH_SERVICE EXCEPTION #======================#
    "MetaHashServiceException",
]


# ======================# META_HASH_SERVICE EXCEPTION #======================#
class MetaHashServiceException(HashServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Basic, Service Primitive

    # PARENT:
        *   HashServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "META_HASH_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HashService raised an exception."