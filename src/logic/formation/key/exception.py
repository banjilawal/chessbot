# src/logic/formation/exception.py

"""
Module: logic.formation.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.system import ContextException

__all__ = [
    # ======================# FORMATION_KEY EXCEPTION #======================#
    "FormationKeyException",
]


# ======================# FORMATION_KEY EXCEPTION #======================#
class FormationKeyException(ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by OrderContext objects.
    2.  Super for conditions which are not covered by lower level OrderContext exceptions.

    # PARENT:
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_KEY_EXCEPTION"
    DEFAULT_ERR_CODE = "OrderContext raised an exception."