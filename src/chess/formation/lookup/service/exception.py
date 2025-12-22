___all__ = [
    # ======================# FORMATION_LOOKUP_SERVICE EXCEPTION #======================#
    "FormationLookupServiceException",
]

from chess.formation import FormationLookupException
from chess.system import ServiceException


# ======================# FORMATION_LOOKUP_SERVICE EXCEPTION #======================#
class FormationLookupServiceException(FormationLookupException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an FormationLookupService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a FormationLookupService method.

    # PARENT:
        *   ServiceException
        *   FormationLookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_LOOKUP_SERVICE_ERROR"
    DEFAULT_MESSAGE = "FormationLookupService raised an exception."