# src/chess/token/exception.py

"""
Module: chess.token.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN EXCEPTION #======================#
    "TokenException",
]

from chess.system import ChessException


# ======================# TOKEN EXCEPTION #======================#
class TokenException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Token errors not covered by TokenException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_ERROR"
    DEFAULT_MESSAGE = "Token raised an exception."