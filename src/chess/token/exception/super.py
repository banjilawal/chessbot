# src/chess/token/exception.py

"""
Module: chess.token.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN EXCEPTION #======================#
    "TokenException",
]

from chess.system import SuperClassException


# ======================# TOKEN EXCEPTION #======================#
class TokenException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of TokenDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "TOKEN_ERROR"
    MSG = "Token raised an exception."