# src/logic/vector/validation/exception/debug/x/null.py

"""
Module: logic.vector.validation.exception.debug.x.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
#======================# VECTOR_NULL_X_AXIS_EXCEPTION #======================#
    "VectorNullXException",
]

from logic.system import NullException

#======================# VECTOR_NULL_X_AXIS_EXCEPTION #======================#
class VectorNullXException(NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a vector.x  was null.
    
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
    ERR_CODE = "VECTOR_NULL_X_AXIS_EXCEPTION"
    MSG = "vector.x  is null."
    
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





