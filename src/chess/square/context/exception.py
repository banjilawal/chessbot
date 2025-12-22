# src/chess/square/exception.py

"""
Module: chess.square.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""


from chess.system import ContextException

__all__ = [
    #======================# SQUARE_CONTEXT EXCEPTION #======================#
    "SquareContextException",
]


#======================# SQUARE_CONTEXT EXCEPTION #======================#
class SquareContextException(ContextException):
    ERROR_CODE = "SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext raised an exception."
    