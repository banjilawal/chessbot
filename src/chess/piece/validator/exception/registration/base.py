# src/chess/piece/validator/exception/registration/base.py

"""
Module: chess.piece.validator.exception.registration.base
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import InvalidPieceException
from chess.system import RegistrationException

__all__ = [
    # ======================# PIECE_REGISTRATION EXCEPTION SUPER CLASS #======================#
    "PieceRegistrationException"
]


# ======================# PIECE_REGISTRATION EXCEPTION SUPER CLASS #======================#
class PieceRegistrationException(InvalidPieceException, RegistrationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall Exception for when an Piece has set its owner correctly but the owner does not
        have the piece in its collection.

    # PARENT:
        *   InvalidPieceException
        *   RegistrationException

    # PROVIDES:
    PieceRegistrationException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Piece not registered with parent."