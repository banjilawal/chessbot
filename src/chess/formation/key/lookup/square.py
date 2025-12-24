# src/chess/formation/validator/exception/square.py

"""
Module: chess.formation.validator.exception.square
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# FORMATION_SQUARE_BOUNDS EXCEPTION #======================#
    "FormationLookupBySquareException",
]


# ======================# FORMATION_SQUARE_BOUNDS EXCEPTION #======================#
class FormationLookupBySquareException(InvalidFormationException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that no opening formation is made from the square.
    1.  Indicate that searching Formations by a Square  Formation forward lookup by forward lookup on the Formation table by a designation came up empty. No Piece is assigned that
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
    ERROR_CODE = "FORMATION_SQUARE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        "No Formation is associated with the Square. No Piece makes its opening move from the Square."
    )


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
