# src/logic/pair/pair/validation/exception/validator.py

"""
Module: logic.pair.pair.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAIR_VALIDATION_FAILURE #======================#
    "PairValidationException",
]

from system import ValidationException

# ======================# PAIR_VALIDATION_FAILURE #======================#
class PairValidationException(ValidationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the PairValidator method where the exception failed.

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
        *   mthd_rslt (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ValidationException class for inherited methods.
    """
    MTHD_RSLT = "ValidationResult"
    ERR_CODE = "PAIR_VALIDATION_FAILURE"
    MSG = "Failure in PairValidator method."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )