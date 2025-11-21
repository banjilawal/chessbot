# src/chess/system/err/binding.py

"""
Module: chess.system.err.binding
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system.err import ChessException


__all__ = [
    "NoBindingException",
]


class NoBindingException(ChessException):
    """"""
    ERROR_CODE = "NO_BINDING_ERROR"
    DEFAULT_MESSAGE = "There is no binding between the two entities. An event cannot be fired."
