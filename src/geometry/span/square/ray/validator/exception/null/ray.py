# src/logic/ray/square/ray/validation/exception/debug/ray.py

"""
Module: logic.ray.square.ray.validation.exception.debug.ray
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_RAY_NULL_EXCEPTION #======================#
    "SquareRayNullException",
]

from logic.system import NullException


# ======================# SQUARE_RAY_NULL_EXCEPTION #======================#
class SquareRayNullException(NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a SquareRay is null where it should not be.

    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    Attributes:
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
    MSG = "SquareRay cannot be null."
    ERR_CODE = "SQUARE_RAY_NULL_EXCEPTION"
    
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
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)