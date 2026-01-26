# src/chess/occupant/validator/exception/registration/board.py

"""
Module: chess.occupant.validator.exception.registration.board
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""




__all__ = [
    #======================# TOKEN_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "TokenNotRegisteredWithBoardException"
]

from chess.token import TokenNotRegisteredException


#======================# TOKEN_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class TokenNotRegisteredWithBoardException(TokenNotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Token has assigned itself to a Board instance, the Board does not
        find the item in board.tokens.

    # PARENT:
        *   TokenNotRegisteredException

    # PROVIDES:
    TokenNotRegisteredWithBoardException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = (
        "Token is not registered in Board.tokens collection. Only the occupant-side of the relationship is set."
    )