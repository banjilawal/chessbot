# src/chess/system/err/null.py

"""
Module: chess.system.err.null
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
#======================# NULL EXCEPTION #======================#
    "NullException",
]

from chess.system import DebugException


#======================# NULL EXCEPTION #======================#
class NullException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Parent of exception that indicate an entity, method, or operation requires an object
        or resource but  but got null instead.
    3.  Catchall for null errors not covered by lower level NullException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_ERROR"
    MSG = "cannot be null."
    





