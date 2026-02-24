# src/chess/rank/validator/exception/wrapper.py

"""
Module: chess.rank.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# RANK_VALIDATION_FAILURE #======================#
    "RankValidationException",
]


# ======================# RANK_VALIDATION_FAILURE #======================#
class RankValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in RankValidator.validate that, prevented ValidationResult.success() 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Rank validation failed."