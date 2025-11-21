# src/chess/rank/validator/collision.py

"""
Module: chess.rank.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import ValidationException

__all__ = [
  "InvalidRankException"
]

# ======================# RANK VALIDATION EXCEPTIONS #======================#
class InvalidRankException(RankException, ValidationException):
  """Catchall Exception for RankValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "RANK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Rank validation failed."

