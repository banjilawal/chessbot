# src/chess/rank/validator/exception.py

"""
Module: chess.rank.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import ValidationFailedException

__all__ = [
  # ======================# RANK_VALIDATION_FAILURE EXCEPTION #======================#
  "RankValidationFailedException",
]


# ======================# RANK_VALIDATION_FAILURE EXCEPTION #======================#
class RankValidationFailedException(RankException, ValidationFailedException):
  """
  # ROLE: Exception Wrapper

  # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Rank. The encapsulated
        exceptions create a chain for tracing the source of the failure.
  # PARENT:
      *   RankException
      *   ValidationFailedException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "RANK_VALIDATION_FAILURE"
  DEFAULT_MESSAGE = "Rank validation failed."