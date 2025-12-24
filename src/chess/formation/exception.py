# src/chess/formation/exception.py

"""
Module: chess.formation.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "FormationException",
]


class FormationException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Formation objects.
    2.  Catchall for conditions which are not covered by lower level Formation exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_ERROR"
    DEFAULT_MESSAGE = "Formation raised an exception."
