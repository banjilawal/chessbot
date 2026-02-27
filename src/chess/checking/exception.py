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
    ERR_CODE = "CHECKING_EXCEPTION"
    MSG = "Checking raised an exception."