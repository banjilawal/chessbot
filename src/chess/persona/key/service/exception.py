# src/chess/persona/key/service/exception.py

"""
Module: chess.persona.key.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

___all__ = [
    # ======================# PERSONA_KEY_SERVICE EXCEPTION #======================#
    "PersonaSuperKeyServiceException",
]

from chess.persona import PersonaSuperKeyException
from chess.system import ServiceException


# ======================# PERSONA_KEY_SERVICE EXCEPTION #======================#
class PersonaSuperKeyServiceException(PersonaSuperKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PersonaKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PersonaSuperKeyService method.

    # PARENT:
        *   ServiceException
        *   PersonaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PersonaSuperKeyService raised an exception."