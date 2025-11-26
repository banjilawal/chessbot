# src/chess/system/err/registration.py

"""
Module: chess.system.err.registration
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system.err import ChessException


__all__ = [
    "RegistrationException",
]


class RegistrationException(ChessException):
    """"""
    ERROR_CODE = "REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "There is no relationship between the entities."
