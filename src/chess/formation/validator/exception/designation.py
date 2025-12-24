# src/chess/formation/validator/exception/name.py

"""
Module: chess.formation.validator.exception.name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# FORMATION_LOOKUP_BY_DESIGNATION_FAILURE EXCEPTION #======================#
    "DesignationFormationLookupException",
]


# ======================# FORMATION_LOOKUP_BY_DESIGNATION_FAILURE EXCEPTION #======================#
class DesignationFormationLookupException(InvalidFormationException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a forward lookup on the Formation table by a designation came up empty. No Piece is assigned that
        designation.

    # PARENT:
        *   InvalidFormationException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_LOOKUP_BY_DESIGNATION_FAILURE"
    DEFAULT_MESSAGE = "No Formation assigns that designation to a Piece. The designation is not valid."
