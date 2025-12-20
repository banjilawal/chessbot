# src/chess/system/err/null.py

"""
Module: chess.system.err.null
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
#======================# NULL EXCEPTION #======================#
    "NullException",
]


#======================# NULL EXCEPTION #======================#
class NullException(ChessException):
    """Raised if an entity, method, or operation requires a resource but gets null instead."""
    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null."
    





