# src/chess/persona/service/exception.py

"""
Module: chess.persona.service.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA_SERVICE EXCEPTION #======================#
    "PersonaServiceException",
]

from chess.persona import PersonaException
from chess.system import ServiceException


# ======================# PERSONA_SERVICE EXCEPTION #======================#
class PersonaServiceException(PersonaException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an PersonaService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a PersonaService method.

    # PARENT:
        *   ServiceException
        *   PersonaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PersonaService raised an exception."