# src/logic/span/square/ray/validator/exception/debug/ray.py

"""
Module: logic.span.square.ray.validator.exception.debug.ray
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
#======================# NULL_SQUARE_RAY_EXCEPTION #======================#
    "NullSquareRayException",
]

from logic.system import NullException

#======================# NULL_SQUARE_RAY_EXCEPTION #======================#
class NullSquareRayException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a squareRay is null where it should not be.
    
    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        val: Optional[Any]
        var: Optional[str]
        msg: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "SquareRay cannot be null."
    ERR_CODE = "NULL_SQUARE_RAY_EXCEPTION"
    
    def __init__(
            self,
            val: Optional[Any] = None,
            var: Optional[str] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,

    ):
        """
        Args:
            val: Optional[Any]
            var: Optional[str]
            msg: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





