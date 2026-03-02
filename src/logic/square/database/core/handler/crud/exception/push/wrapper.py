# src/logic/square/service/collision/exception/debug/wrapper.py

"""
Module: logic.square.service.collision.exception.debug.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_STACK_PUSH_FAILURE #======================#
    "SquareStackPushException",
]

from logic.system import InsertionException

# ======================# SQUARE_STACK_PUSH_FAILURE #======================#
class SquareStackPushException(InsertionException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the SquareStackService method where the push failed.
        
    # PARENT:
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See InsertionException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See InsertionException class for inherited methods.
    """
    MTHD = None
    OP = "Insert"
    RSLT_TYPE = "InsertionResult"
    MSG = "SquareStack push failed."
    ERR_CODE = "SQUARE_STACK_PUSH_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )