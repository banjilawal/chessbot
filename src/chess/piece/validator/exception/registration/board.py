# src/chess/piece/number_bounds_validator/exception/registration/board.py

"""
Module: chess.piece.number_bounds_validator.exception.registration.board
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import  PieceRegistrationException


__all__ = [
    #======================# PIECE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "PieceNotRegisteredWithBoardException"
]

#======================# PIECE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class PieceNotRegisteredWithBoardException(PieceRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Piece has assigned itself to a Board instance, the Board does not
        find the item in board.pieces.

    # PARENT:
        *   PieceRegistrationException

    # PROVIDES:
    PieceNotRegisteredWithBoardException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = (
        "Piece is not registered in Board.pieces collection. Only the piece-side of the relationship is set."
    )