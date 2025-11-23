# src/chess/square/context/exception.py

"""
Module: chess.square.context.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from chess.system import SearchContextException

__all__ = [
    # ======================# SQUARE_CONTEXT EXCEPTIONS #======================#
    "SquareContextException",
]


# ======================# SQUARE_CONTEXT EXCEPTIONS #======================#
class SquareContextException(SearchContextException):
    ERROR_CODE = "SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext raised an exception."
    