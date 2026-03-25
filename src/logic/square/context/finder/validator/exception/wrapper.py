# src/logic/square/validation/exception/work.py

"""
Module: logic.square.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_LIST_VALIDATION_FAILURE #======================#
    "SquareListValidationException",
]

from logic.system import ValidationException


# ======================# SQUARE_LIST_VALIDATION_FAILURE #======================#
class SquareListValidationException(ValidationException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate a SquareValidation was unsuccessful and did not produce a result.
        2.  Identify the SquareListValidationException method where the failure occurred.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super Class:
        ValidationException
    """
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    ERR_CODE = "SQUARE_LIST_VALIDATION_FAILURE"
    MSG = "Failure in SquareListValidationProcess method."
    
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