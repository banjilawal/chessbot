# src/chess/formation/key/lookup/exception/debug/persona.py

"""
Module: chess.formation.key.lookup.exception.debug.persona
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.formation import FormationException

__all__ = [
    # ======================# FORMATION_PERSONA_BOUNDS EXCEPTION #======================#
    "FormationPersonaBoundsException",
]


# ======================# FORMATION_PERSONA_BOUNDS EXCEPTION #======================#
class FormationPersonaBoundsException(FormationException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Formation lookup failed because the persona value was not permitted for the Formation
        attribute.

    # PARENT:
        *   FormationException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_PERSONA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "FormationLookup failed: Target was outside the set of possible Formation personas."
