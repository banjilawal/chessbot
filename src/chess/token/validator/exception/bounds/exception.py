# src/chess/token/validator/exception/bounds/exception.py

"""
Module: chess.token.validator.exception.bounds.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import BoundsException
from chess.token import TokenException

__all__ = [
    #======================# TOKEN BOUNDS EXCEPTION #======================#
    "TokenAttributeBoundsException",
    "RosterNumberOutOfBoundsException",
    "TokenRankOutOfBoundsException",
    "TokenNameOutOfBoundsException",
]

#======================# TOKEN BOUNDS EXCEPTION #======================#
class TokenAttributeBoundsException(TokenException, BoundsException):
    """Raised if a Token attribute is outside its Layout or Rank settings."""
    ERROR_CODE = "TOKEN_ATTRIBUTE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token attribute is out of bounds."


class RosterNumberOutOfBoundsException(TokenAttributeBoundsException):
    """Raised if a Token's roster number < 1 or > TEAM_SIZE."""
    ERROR_CODE = "ROSTER_NUMBER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.roster_number out of bounds."


class TokenRankOutOfBoundsException(TokenAttributeBoundsException):
    """Raised a Token's rank is out of bounds."""
    ERROR_CODE = "TOKEN_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.rank is out of bounds."


class TokenNameOutOfBoundsException(TokenAttributeBoundsException):
    """Raised a Token's designation is out of bounds specified in LayoutSchema."""
    ERROR_CODE = "TOKEN_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.designation is out of bounds."