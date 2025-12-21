# src/chess/system/context/exception/flag.py

"""
Module: chess.system.context.exception.flag
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException, ContextException

__all__ = [
    # ======================# CONTEXT_FLAG_COUNT EXCEPTION #======================#
    "ContextFlagCountException",
]


# ======================# CONTEXT_FLAG_COUNT EXCEPTION #======================#
class ContextFlagCountException(ContextException, BoundsException):
    """
    # ROLE: Exception Wrapper, Catchall Exception,
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions which indicate the attributee-value flags enabled in a Context is out of bounds.
    2.  Catchall for ContextFlagCount errors not covered by lower level ContextFlagEception exceptions.
  
      # PARENT
        *   BoundsException
        *   ContextException

      # PROVIDES:
      None

      # LOCAL ATTRIBUTES:
      None

      # INHERITED ATTRIBUTES:
      None
      """
    ERROR_CODE = "CONTEXT_FLAG_COUNT_ERROR"
    DEFAULT_MESSAGE = "The number of Context attribute-value flags enabled is out of bounds."
