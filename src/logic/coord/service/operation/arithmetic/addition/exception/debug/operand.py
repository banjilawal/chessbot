# src/logic/token/service/operation/arithmetic/addition/exception/debug/operand.py

"""
Module: logic.token.service.operation.arithmetic.addition.exception.debug.operand
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COORD_ADDITION_OPERAND_NULL_EXCEPTION #======================#
    "CoordAdditionOperandNullException",
]

from logic.coord import CoordDebugException


# ======================# COORD_ADDITION_OPERAND_NULL_EXCEPTION #======================#
class CoordAdditionOperandNullException(CoordDebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate a CoordAdditionTransaction failed because the operand was null
            instead of Union[Vector, Coord].
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        CoordDebugException
    """
    ERR_CODE = "COORD_ADDITION_OPERAND_NULL_EXCEPTION"
    MSG = "CoordAdditionTransaction: Operand is null."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)