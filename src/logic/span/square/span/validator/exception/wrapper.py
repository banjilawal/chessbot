# src/logic/span/square/span/validator/exception/wrapper.py

"""
Module: logic.span.square.span.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-03-12
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_SPAN_VALIDATION_FAILURE #======================#
    "SquareSpanValidationException",
]

from logic.system import ValidationException

# ======================# SQUARE_SPAN_VALIDATION_FAILURE #======================#
class SquareSpanValidationException(ValidationException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identify the SquareSpanValidator method where the process failed.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ValidationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        op: Optional[str]
        msg: Optional[str]
        ex: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ValidationException class for inherited methods.
    """
    MTHD = Optional[str]
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    ERR_CODE = "SQUARE_SPAN_VALIDATION_FAILURE"
    MSG = "Failure in SquareSpanValidator method."

    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            ex: Optional[str]
            mthd: Optional[str]
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