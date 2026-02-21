# src/chess/rank/validator/exception.py

"""
Module: chess.rank.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import ValidationException

__all__ = [
  # ======================# RANK_VALIDATION_FAILURE EXCEPTION #======================#
    "RankValidationException",
]


# ======================# RANK_VALIDATION_FAILURE EXCEPTION #======================#
class RankValidationException(RankException, ValidationException):
  """
  # ROLE: Exception Wrapper

  # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Rank. The exception chain traces the ultimate source of failure.
  # PARENT:
      *   RankException
      *   ValidationException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "RANK_VALIDATION_FAILURE"
  DEFAULT_MESSAGE = "Rank validation failed."