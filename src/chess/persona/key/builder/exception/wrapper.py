# src/chess/persona/builder/wrapper.py

"""
Module: chess.persona.builder.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BuildException
from chess.persona import PersonaKeyException


__all__ = [
    # ======================# PERSONA_CONTEXT BUILD EXCEPTION #======================#
    "PersonaKeyBuildException",
]


# ======================# PERSONA_CONTEXT BUILD EXCEPTION #======================#
class PersonaKeyBuildException(PersonaKeyException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during PersonaKey build process.
    2.  Wrap an exception that hits the try-finally block of an PersonaKeyBuilder method.

    # PARENT:
        *   PersonaKeyException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "PersonaKey build failed."