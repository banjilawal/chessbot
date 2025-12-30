___all__ = [
    # ======================# PERSONA_LOOKUP_SERVICE EXCEPTION #======================#
    "PersonaLookupServiceException",
]

from chess.agent import AgentException
from chess.system import ServiceException


# ======================# PERSONA_LOOKUP_SERVICE EXCEPTION #======================#
class PersonaLookupServiceException(PersonaLookupException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PersonaLookupService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PersonaLookupService method.

    # PARENT:
        *   ServiceException
        *   PersonaLookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_LOOKUP_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PersonaLookupService raised an exception."