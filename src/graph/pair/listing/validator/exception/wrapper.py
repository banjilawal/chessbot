# src/logic/pair/listing/validation/exception/validator.py

"""
Module: logic.pair.listing.validation.exception.work
Author: Banji Lawal
Created: 2026-03-12
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAIR_LIST_VALIDATION_FAILURE #======================#
    "PairListValidatorException",
]

from system import ValidatorException

# ======================# PAIR_LIST_VALIDATION_FAILURE #======================#
class PairListValidatorException(ValidatorException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the PairListValidator method where the exception failed.

    Super Class:
        *   ValidatorException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ValidatorException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ValidatorException class for inherited methods.
    """
    MTHD_RSLT = "ValidationResult"
    ERR_CODE = "PAIR_LIST_VALIDATION_FAILURE"
    MSG = "Failure in PairListValidator method."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
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