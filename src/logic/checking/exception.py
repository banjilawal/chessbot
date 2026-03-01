# src/logic/checking/checking.py

"""
Module: logic.checking.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""


from logic.system import ChessException

__all__ = [
    "CheckingException",
]

class CheckingException(ChessException):
    ERR_CODE = "CHECKING_EXCEPTION"
    MSG = "Checking raised an exception."