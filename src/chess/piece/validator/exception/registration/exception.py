# src/chess/piece/validator/exception/registration/registration.py

"""
Module: chess.piece.validator.exception.registration.registration
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import InvalidPieceException
from chess.system import RegistrationException

__all__ = [
    # ======================# PIECE_REGISTRATION EXCEPTIONS #======================#
    "PieceRegistrationException",
    "PieceNotRegisteredWithBoardException",
    "PieceNotRegisteredWithSquareException",
    "PieceNotRegisteredWithTeamException",
]


# ======================# PIECE_REGISTRATION EXCEPTIONS #======================#
class PieceRegistrationException(InvalidPieceException, RegistrationException):
    """
    Catchall for when a Piece does not have a relationship with another entity.
    """
    ERROR_CODE = "PIECE_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Piece is not registered in the collection."


class PieceNotRegisteredWithBoardException(PieceRegistrationException):
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = (
        "Piece is not registered in Board.pieces collection. There is no relationship between them."
    )


class PieceNotRegisteredWithSquareException(PieceRegistrationException):
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_SQUARE_ERROR"
    DEFAULT_MESSAGE = (
        "Piece is not registered as Square.occupant. There is no relationship between them."
    )


class PieceNotRegisteredWithTeamException(PieceRegistrationException):
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_TEAM_ERROR"
    DEFAULT_MESSAGE = (
        "Piece is not registered in Team.roster. There is no relationship between them."
    )
