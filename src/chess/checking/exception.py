# src/chess/checking/checking.py

"""
Module: chess.checking.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""


from chess.system import ChessException

__all__ = [
    "CheckingException",
]

class CheckingException(ChessException):
    ERROR_CODE = "CHECKING_ERROR"
    DEFAULT_MESSAGE = "Checking raised an exception."