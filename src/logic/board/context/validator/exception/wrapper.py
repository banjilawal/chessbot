# src/logic/board/validation/exception/exception.py

"""
Module: logic.board.validation.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# BOARD_CONTEXT_VALIDATION_FAILURE #======================#
    "BoardContextValidationException",
]

from logic.system import ValidationException

# ======================# BOARD_CONTEXT_VALIDATION_FAILURE #======================#
class BoardContextValidationException(ValidationException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the BoardValidator method where the exception failed.

    Super Class:
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ValidationException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ValidationException class for inherited methods.
    """
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    ERR_CODE = "BOARD_CONTEXT_VALIDATION_FAILURE"
    MSG = "Failure in BoardValidator method."
    
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