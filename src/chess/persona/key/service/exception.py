# src/chess/persona/key/service/exception.py

"""
Module: chess.persona.key.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

___all__ = [
    # ======================# PERSONA_KEY_SERVICE EXCEPTION #======================#
    "PersonaKeyServiceException",
]

from chess.persona import PersonaKeyException
from chess.system import ServiceException


# ======================# PERSONA_KEY_SERVICE EXCEPTION #======================#
class PersonaKeyServiceException(PersonaKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PersonaKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PersonaKeyService method.

    # PARENT:
        *   ServiceException
        *   PersonaKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PersonaKeyService raised an exception."