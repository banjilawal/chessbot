# src/geometry/span/square/ray/validation/exception/validator.py

"""
Module: geometry.span.square.ray.validation.exception.work
Author: Banji Lawal
Created: 2026-03-12
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_RAY_VALIDATION_FAILURE #======================#
    "SquareRayValidationException",
]

from system import ValidationException

# ======================# SQUARE_RAY_VALIDATION_FAILURE #======================#
class SquareRayValidationException(ValidationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the SquareRayValidator method where the exception failed.

    Super Class:
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ValidationException class for inherited attributes.

    Attributes:
        msg: Optional[str]
        ex: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ValidationException class for inherited methods.
    """
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    ERR_CODE = "SQUARE_RAY_VALIDATION_FAILURE"
    MSG = "Failure in SquareRayValidator method."

    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[ResultCategory]
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