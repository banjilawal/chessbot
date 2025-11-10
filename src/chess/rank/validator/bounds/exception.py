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

# ======================# RANK_RANSOM_FIELD VALIDATION EXCEPTIONS #======================#
    "RankRansomException",
    "NullRankRansomException",
    "RankRansomBelowBoundsException",
    "RankRansomAboveBoundsException",

# ======================# RANK_QUOTA_FIELD VALIDATION EXCEPTIONS #======================#
    "RankQuotaException",
    "NullRankQuotaException",
    "RankQuotaBelowBoundsException",
    "RankQuotaAboveBoundsException",

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

# ======================# RANK_RANSOM_FIELD VALIDATION EXCEPTIONS #======================#
class RankRansomException(RankBoundsException):
    ERROR_CODE = "RANK_RANSOM_FIELD_ERROR"
    DEFAULT_MESSAGE = "The visitor_ransom of a Rank object is outside the bounds declared in RankSpec."

class NullRankRansomException(RankRansomException, NullException):
    ERROR_CODE = "NULL_RANK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "A Rank object cannot have a null visitor_ransom."

class RankRansomBelowBoundsException(RankRansomException):
    ERROR_CODE = "RANK_RANSOM_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Rank instance cannot have a negative visitor_ransom value. The lowest visitor_ransom allowed is zero."

class RankRansomAboveBoundsException(RankRansomException):
    ERROR_CODE = "RANK_RANSOM_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Queen bounds has the highest allowable visitor_ransom. The value is above the visitor_ransom bounds."


# ======================# RANK_QUOTA_FIELD VALIDATION EXCEPTIONS #======================#
class RankQuotaException(RankBoundsException):
    ERROR_CODE = "RANK_QUOTA_FIELD_ERROR"
    DEFAULT_MESSAGE = "The quota of a Rank object is outside the bounds declared in RankSpec."

class NullRankQuotaException(RankQuotaException, NullException):
    ERROR_CODE = "NULL_RANK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "A Rank object cannot have a null quota."

class RankQuotaBelowBoundsException(RankQuotaException):
    ERROR_CODE = "RANK_QUOTA_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Rank instance cannot have a quota below one."

class RankQuotaAboveBoundsException(RankQuotaException):
    ERROR_CODE = "RANK_QUOTA_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Pawn has the highest quota. The value is above quota bounds."


# ======================# RANK_NAME_FIELD VALIDATION EXCEPTIONS #======================#
class RankNameException(RankException):
    ERROR_CODE = "RANK_NAME_FIELD_ERROR"
    DEFAULT_MESSAGE = "Name field of a Rank object raised an exception."

class RankNameOutOfBoundsException(RankBoundsException):
    ERROR_CODE = "RANK_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The visitor_name is not included in the Rank visitor_name specifications."


# ======================# RANK_LETTER_FIELD VALIDATION EXCEPTIONS #======================#
class RankLetterException(InvalidRankException):
    ERROR_CODE = "RANK_LETTER_FIELD_ERROR"
    DEFAULT_MESSAGE = "The letter field of a Rank object raised an exception."

class NullRankLetterException(RankLetterException, NullException):
    ERROR_CODE = "NULL_RANK_LETTER_ERROR"
    DEFAULT_MESSAGE = "A Rank object cannot have a null letter field."

class RankLetterOutOfBoundsException(RankBoundsException):
    ERROR_CODE = "RANK_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"The letter is not included in the Rank letter specifications."


# ======================# RANK_ID_FIELD VALIDATION EXCEPTIONS #======================#
class RankIdException(RankException):
    ERROR_CODE = "RANK_ID_FIELD_ERROR"
    DEFAULT_MESSAGE = "The visitor_id field of a Rank object raised an exception."

class RankIdAboveBoundsException(RankIdException):
    ERROR_CODE = "RANK_ID_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"The value is too high for a Rank visitor_id."