___all__ = [
    # ======================# SCHEMA_LOOKUP EXCEPTION #======================#
    "SchemaLookupException",
]

from chess.agent import AgentException
from chess.system import ServiceException


# ======================# SCHEMA_LOOKUP EXCEPTION #======================#
class SchemaLookupException(SchemaLookupException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaForwardLookup encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaForwardLookup method.

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
    ERROR_CODE = "SCHEMA_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "SchemaForwardLookup raised an exception."