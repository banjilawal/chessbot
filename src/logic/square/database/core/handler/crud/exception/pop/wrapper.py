# src/logic/square/database/core/exception/deletion/wrapper.py

"""
Module: logic.square.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_STACK_POP_FAILURE #======================#
    "SquareStackPopException",
]

from logic.system import DeletionException


# ======================# SQUARE_STACK_POP_FAILURE #======================#
class SquareStackPopException(DeletionException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the SquareStackService method where the pop failed.

    # PARENT:
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DeletionException class for inherited attributes.

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
        *   See DeletionException class for inherited methods.
    """
    MTHD = None
    OP = "Delete"
    RSLT_TYPE = "DeletionResult"
    MSG = "SquareStack pop failed."
    ERR_CODE = "SQUARE_STACK_POP_FAILURE"
    
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