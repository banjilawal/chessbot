# src/chess/rank/spec/collision.py
"""
Module: chess.rank.spec.exception
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""
from chess.rank import RankException
from chess.system import BoundsException, ChessException, NullException, ValidationException

__all__ = [
    # ======================# RANK_SPEC EXCEPTION SUPER CLASS #======================#
    "RankSpecException",
    
    # ======================# RANK_SPEC VALIDATION EXCEPTIONS #======================#
    "InvalidRankSpecException",
    "NullRankSpecException",
    
    # ======================# RANK_SPEC BOUNDS EXCEPTIONS #======================#
    "RankNameBoundsException",
    "RankColorBoundsException",
]


# ======================# RANK_SPEC EXCEPTION SUPER CLASS #======================#
class RankSpecException(RankException):
    """
    Super class of all exceptions RankSpec object raises. Do not use directly. Subclasses give
    details useful for debugging.
    """
    ERROR_CODE = "RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec raised an exception."


# ======================# RANK_SPEC VALIDATION EXCEPTIONS #======================#
class InvalidRankSpecException(RankSpecException, ValidationException):
    """
    Raised by RankSpecValidator if an object fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existingRankSpec.
    """
    ERROR_CODE = "RANK_SPEC_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "RankSpec validation failed."


class NullRankSpecException(RankSpecException, NullException):
    """Raised if an entity, method, or operation requires a RankSpec but gets null."""
    ERROR_CODE = "NULL_RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec cannot be null."


# ======================# RANK_SPEC BOUNDS EXCEPTIONS #======================#
class RankIdBoundsException(RankSpecException, BoundsException):
    """Raised if a number is not in a RankSpec ids."""
    ERROR_CODE = "RANK_ID_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Number is outside the range of Rank.ids allowed in RankSpec."
    
    
class RankNameBoundsException(RankSpecException, BoundsException):
    """Raised if a value is not in a RankSpec names."""
    ERROR_CODE = "RANK_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "String is outside the range of Rank.names allowed in RankSpec."


class RankDesignationBoundsException(RankSpecException, BoundsException):
    """Raised if a string is not in a RankSpec designations."""
    ERROR_CODE = "RANK_DESIGNATION_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "String is outside the range of Rank.designations allowed in RankSpec."


class RankRansomBoundsException(RankSpecException, BoundsException):
    """Raised if a number is not in a RankSpec ransoms."""
    ERROR_CODE = "RANK_RANSOM_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Number is outside the range of Rank.ransoms allowed in RankSpec."


class RankQuotaBoundsException(RankSpecException, BoundsException):
    """Raised if a value is not in a RankSpec team_quotas."""
    ERROR_CODE = "RANK_QUOTA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Number is outside the range of Rank.team_quotas allowed in RankSpec."