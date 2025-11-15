# src/chess/bounds/validator/bounds/exception.py

"""
Module: chess.bounds.validator.bounds.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.rank import RankException, InvalidRankException
from chess.system import NullException, ValidationException

__all__ = [
    "RankBoundsException",



#

# ======================# RANK_NAME_FIELD VALIDATION EXCEPTIONS #======================#
    "RankNameException",
    "RankNameOutOfBoundsException",

# ======================# RANK_LETTER_FIELD VALIDATION EXCEPTIONS #======================#
    "RankLetterException",
    "NullRankLetterException",
    "RankLetterOutOfBoundsException",

# ======================# RANK_ID_FIELD VALIDATION EXCEPTIONS #======================#
    "RankIdException",
    "RankIdAboveBoundsException",
]


class RankBoundsException(InvalidRankException):
    ERROR_CODE = "RANK_FIELD_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The field of a Rank object is outside the bounds declared in RankSpec."










