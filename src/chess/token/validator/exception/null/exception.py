# src/chess/piece/validator/exception/null/exception.py

"""
Module: chess.piece.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import NullException
from chess.piece import InvalidPieceException

__all__ = [
    "NullPieceException",
    "PieceTeamFieldIsNullException",
    "PieceNullCoordStackException",
    "PieceRosterNumberIsNullException",
]


#======================# PIECE NULL EXCEPTION #======================#
class NullPieceException(InvalidPieceException, NullException):
    """Raised if an entity, method, or operation expects a Token but gets null instead."""
    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Token cannot be null."


class PieceTeamFieldIsNullException(NullPieceException):
    """
    Raised if Token.team does not exist. This field is set during the build and
    should never be null. A null team attribute indicate that  there amy be a fatal application error.
    """
    ERROR_CODE = "PIECE_TEAM_FIELD_NULL_ERROR"
    DEFAULT_MESSAGE = "Token.team field cannot be null. There may be a fatal application error."
    

class PieceNullCoordStackException(NullPieceException):
    """
    Raised if Token.positions does not exist. This field is set during the build and
    should never be null. A null positions attribute indicate that  there amy be a fatal application error.
    """
    ERROR_CODE = "PIECE_COORD_STACK_MISSING_ERROR"
    DEFAULT_MESSAGE = "Token.positions cannot be null. There may be a fatal application error."


class PieceRosterNumberIsNullException(NullPieceException):
    """
    Raised if a Token.roster_number attribute is null. This field is set during the build and
    should never be null. A null positions attribute indicate that  there amy be a fatal application error.
    """
    ERROR_CODE = "PIECE_NULL_ROSTER_NUMBER_ERROR"
    DEFAULT_MESSAGE = "Token.roster_number cannot be null. There may be a fatal application error."
