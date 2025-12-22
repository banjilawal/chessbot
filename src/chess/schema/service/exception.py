from chess.system import ServiceException
from chess.schema import SchemaException

__all__ = [
    # ======================# SCHEMA_SERVICE EXCEPTION #======================#
    "SchemaServiceException",
]


# ======================# SCHEMA_SERVICE EXCEPTION #======================#
class SchemaServiceException(SchemaException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaService method.

    # PARENT:
        *   ServiceException
        *   SchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SchemaService raised an exception."