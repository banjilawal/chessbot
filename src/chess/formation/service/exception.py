from chess.system import ServiceException
from chess.formation import FormationException

__all__ = [
    # ======================# FORMATION_SERVICE EXCEPTION #======================#
    "FormationServiceException",
]


# ======================# FORMATION_SERVICE EXCEPTION #======================#
class FormationServiceException(FormationException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an FormationService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a FormationService method.

    # PARENT:
        *   ServiceException
        *   FormationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_SERVICE_ERROR"
    DEFAULT_MESSAGE = "FormationService raised an exception."