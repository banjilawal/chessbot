# src/chess/formation/exception.py

"""
Module: chess.formation.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# FORMATION EXCEPTION #======================#
    "FormationException",
]


# ======================# FORMATION EXCEPTION #======================#
class FormationException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Formation errors not covered by FormationException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_ERROR"
    DEFAULT_MESSAGE = "Formation raised an exception."