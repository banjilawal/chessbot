# src/chess/token/exception.py

"""
Module: chess.token.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [

    "TokenException",
]

from chess.system import ChessException


class TokenException(ChessException):
    ERROR_CODE = "TOKEN__ERROR"
    DEFAULT_MESSAGE = "Token validation failed."