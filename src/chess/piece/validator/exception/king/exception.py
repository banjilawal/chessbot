# src/chess/piece/validator/exception/king/collision.py

"""
Module: chess.piece.validator.exception.king.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.piece import InvalidPieceException


class CheckmatedKingException(InvalidPieceException):
    """
    # RESPONSIBILITY
    Raised when a checkmated king tries to do something.


    # RELATED EXCEPTIONS
        *   AttackException
        *   TravelException
    """
    ERROR_CODE = "CHECK_MATED_KING_EXCEPTION"
    DEFAULT_MESSAGE = "Checkmated king raised an exception."

class CheckmatedKingCannotTravelException(CheckmatedKingException):
    """"""
    ERROR_CODE = "CHECK_MATED_KING_CANNOT_TRAVEL_ERROR"
    DEFAULT_MESSAGE = "Checkmated king cannot travel."


class CheckmatedKingCannotAttackException(CheckmatedKingException):
    """"""
    ERROR_CODE = "CHECK_MATED_KING_CANNOT_TRAVEL_ERROR"
    DEFAULT_MESSAGE = "Checkmated king cannot attack."
    
    
    