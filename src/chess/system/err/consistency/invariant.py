# src/chess/system/err/consistency/invariant.py

"""
Module: chess.system.err.consistency.invariant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# INVARIANT_BREACH EXCEPTION #======================#
    "InvariantBreachException",
]

from chess.system import InconsistencyException


# ======================# INVARIANT_BREACH EXCEPTION #======================#
class InvariantBreachException(InconsistencyException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a fundamental invariant of the system or environment is violated. The system’s
        assumptions about its internal state are no longer valid.

    # PARENT:
        *   InconsistencyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    DEFAULT_CODE = "INVARIANT_BREACH_ERROR"
    DEFAULT_MESSAGE = (
        "A system invariant was violated, indicating a critical state inconsistency. or entity_service loss."
    )