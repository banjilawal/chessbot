___all__ = [
    # ======================# FORMATION_SUPER_KEY_SERVICE EXCEPTION #======================#
    "FormationSuperKeyServiceException",
]

from chess.formation import FormationSuperKeyException
from chess.system import ServiceException


# ======================# FORMATION_SUPER_KEY_SERVICE EXCEPTION #======================#
class FormationSuperKeyServiceException(FormationSuperKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an FormationSuperKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a FormationSuperKeyService method.

    # PARENT:
        *   ServiceException
        *   FormationSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_SUPER_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "FormationSuperKeyService raised an exception."