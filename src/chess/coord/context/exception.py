# src/coord/context/base.py

"""
Module: chess.coord.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ContextException

__all__ = ["CoordContextException"]

class CoordContextException(ContextException):
    """
    Super class of exceptions raised by CoordContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordContext raised an exception."