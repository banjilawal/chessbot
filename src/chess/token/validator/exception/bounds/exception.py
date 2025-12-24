# src/chess/piece/validator/exception/bounds/exception.py

"""
Module: chess.piece.validator.exception.bounds.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import BoundsException
from chess.piece import InvalidPieceException

__all__ = [
    #======================# PIECE BOUNDS EXCEPTION #======================#
    "PieceAttributeBoundsException",
    "RosterNumberOutOfBoundsException",
    "PieceRankOutOfBoundsException",
    "PieceNameOutOfBoundsException",
]

#======================# PIECE BOUNDS EXCEPTION #======================#
class PieceAttributeBoundsException(InvalidPieceException, BoundsException):
    """Raised if a Token attribute is outside its Layout or Rank settings."""
    ERROR_CODE = "PIECE_ATTRIBUTE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token attribute is out of bounds."


class RosterNumberOutOfBoundsException(PieceAttributeBoundsException):
    """Raised if a Token's roster number < 1 or > TEAM_SIZE."""
    ERROR_CODE = "ROSTER_NUMBER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.roster_number out of bounds."


class PieceRankOutOfBoundsException(PieceAttributeBoundsException):
    """Raised a Token's rank is out of bounds."""
    ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.rank is out of bounds."


class PieceNameOutOfBoundsException(PieceAttributeBoundsException):
    """Raised a Token's designation is out of bounds specified in LayoutSchema."""
    ERROR_CODE = "PIECE_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Token.designation is out of bounds."