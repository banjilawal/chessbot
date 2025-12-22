from chess.system import ServiceException
from chess.schema import SchemaLookupException

__all__ = [
    # ======================# SCHEMA_LOOKUP_SERVICE EXCEPTION #======================#
    "SchemaLookupServiceException",
]


# ======================# SCHEMA_LOOKUP_SERVICE EXCEPTION #======================#
class SchemaLookupServiceException(SchemaLookupException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaLookupService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaLookupService method.

    # PARENT:
        *   ServiceException
        *   SchemaLookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_LOOKUP_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SchemaLookupService raised an exception."