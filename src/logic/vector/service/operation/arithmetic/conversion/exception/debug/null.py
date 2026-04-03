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
    # ======================# VECTOR_COORD_CONVERSION_OPERAND_NULL_EXCEPTION #======================#
    "VectorCoordConversionOperandNullException",
]

from logic.coord import NullException


# ======================# VECTOR_COORD_CONVERSION_OPERAND_NULL_EXCEPTION #======================#
class VectorCoordConversionOperandNullException(NullException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that conversion between a coord and vector failed because the
            operand was null.
            
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        NullException
    """
    MSG = "Conversion failed. The operand was null."
    ERR_CODE = "VECTOR_COORD_CONVERSION_OPERAND_NULL_EXCEPTION"
    
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
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )
