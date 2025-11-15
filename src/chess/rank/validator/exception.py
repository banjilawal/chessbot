# src/chess/rank/validator/exception.py

"""
Module: chess.rank.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import NullException, ValidationException

__all__ = [

#======================# RANK VALIDATION EXCEPTIONS #======================#  
  'NullRankException',
  'InvalidRankException'
]

# ======================# RANK VALIDATION EXCEPTIONS #======================#
class NullRankException(RankException, NullException):
  ERROR_CODE = "NULL_RANK_ERROR"
  DEFAULT_MESSAGE = "Rank cannot be null"

class InvalidRankException(RankException, ValidationException):
  ERROR_CODE = "RANK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Rank validation failed."