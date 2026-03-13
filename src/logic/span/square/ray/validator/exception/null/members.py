# src/logic/span/square/ray/validator/exception/debug/null.py

"""
Module: logic.span.square.ray.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional
__all__ = [
    # ======================# SQUARE_RAY_MEMBERS_NULL_EXCEPTION #======================#
    "SquareRayMembersNullException",
]

from logic.system import NullException

# ======================# SQUARE_RAY_MEMBERS_NULL_EXCEPTION #======================#
class SquareRayMembersNullException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a SquareRay candidate was not validated because it's rays
        were null instead of a List[Square]

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
    ERR_CODE = "SQUARE_RAY_MEMBERS_NULL_EXCEPTION"
    MSG = "SquareRay members cannot be null instead of a List[Square]."
    
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