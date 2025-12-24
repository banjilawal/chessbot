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
  "InvalidRankException",
]


# ======================# RANK_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidRankException(RankException, ValidationFailedException):
  """
  # ROLE: Exception Wrapper

  # RESPONSIBILITIES:
  1.  A debug exception is created when a Rank candidate fails a validation test. Validation debug exceptions are
      encapsulated inside an InvalidRankException creating an exception chain. which is sent to the caller in a
      ValidationResult.
  2.  The InvalidRankException chain is useful for tracing a  failure to its source.

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