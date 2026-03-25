# src/logic/pair/pair/validation/exception/work.py

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

from logic.system import ValidationException

# ======================# PAIR_VALIDATION_FAILURE #======================#
class PairValidationException(ValidationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the PairValidationProcess method where the exception failed.

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
    ERR_CODE = "PAIR_VALIDATION_FAILURE"
    MSG = "Failure in PairValidationProcess method."
    
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
            ex: Optional[str]
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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