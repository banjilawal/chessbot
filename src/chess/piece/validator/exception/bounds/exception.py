# src/chess/piece/number_bounds_validator/exception/bounds/exception.py

"""
Module: chess.piece.number_bounds_validator.exception.bounds.exception
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
    """Raised if a Piece attribute is outside its Layout or Rank settings."""
    ERROR_CODE = "PIECE_ATTRIBUTE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Piece attribute is out of bounds."


class RosterNumberOutOfBoundsException(PieceAttributeBoundsException):
    """Raised if a Piece's roster number < 1 or > TEAM_SIZE."""
    ERROR_CODE = "ROSTER_NUMBER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Piece.roster_number out of bounds."


class PieceRankOutOfBoundsException(PieceAttributeBoundsException):
    """Raised a Piece's rank is out of bounds."""
    ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Piece.rank is out of bounds."


class PieceNameOutOfBoundsException(PieceAttributeBoundsException):
    """Raised a Piece's designation is out of bounds specified in LayoutSchema."""
    ERROR_CODE = "PIECE_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Piece.designation is out of bounds."