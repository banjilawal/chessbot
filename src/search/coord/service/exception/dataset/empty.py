# src/logic/square/validation/exception/debug/null.py

"""
Module: logic.square.validation.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
#======================# NULL_SQUARE_EXCEPTION #======================#
    "EmptyCoordDatasetException",
]

from system import NullException

#======================# NULL_SQUARE_EXCEPTION #======================#
class EmptyCoordDatasetException(NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a square is null where it should not be.
    
    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    ERR_CODE = "NULL_SQUARE_EXCEPTION"
    MSG = "Square cannot be null."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





