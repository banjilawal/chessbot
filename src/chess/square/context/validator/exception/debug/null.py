# src/chess/square/validator/exception/debug/y/token.py

"""
Module: chess.square.validator.exception.debug.y.token
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_TOKEN_Y_AXIS EXCEPTION #======================#
    "SquareTokenYException",
]

from chess.system import TokenException

# ======================# SQUARE_TOKEN_Y_AXIS EXCEPTION #======================#
class SquareTokenYException(TokenException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that Square validation failed because the y_axis was token.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "SQUARE_TOKEN_Y_AXIS_ERROR"
    MSG = "Square validation failed: The y_axis was token."
    VAR: None
    VAL: None
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[None] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

