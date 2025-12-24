___all__ = [
    # ======================# CATALOG_LOOKUP_SERVICE EXCEPTION #======================#
    "CatalogLookupServiceException",
]

from chess.agent import AgentException
from chess.system import ServiceException


# ======================# CATALOG_LOOKUP_SERVICE EXCEPTION #======================#
class CatalogLookupServiceException(CatalogLookupException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CatalogLookupService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CatalogLookupService method.

    # PARENT:
        *   ServiceException
        *   CatalogLookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_LOOKUP_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CatalogLookupService raised an exception."