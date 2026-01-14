___all__ = [
    # ======================# FORMATION_KEY_SERVICE EXCEPTION #======================#
    "FormationKeyServiceException",
]

from chess.formation import FormationKeyException
from chess.system import ServiceException


# ======================# FORMATION_KEY_SERVICE EXCEPTION #======================#
class FormationKeyServiceException(FormationKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an FormationKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a FormationKeyService method.

    # PARENT:
        *   ServiceException
        *   FormationKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "FormationKeyService raised an exception."