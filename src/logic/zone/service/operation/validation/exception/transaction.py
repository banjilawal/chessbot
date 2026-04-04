# src/logic/zone/validation/exception/validator.py

"""
Module: logic.zone.validation.exception.work
Author: Banji Lawal
Created: 2026-03-29
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ZONE_VALIDATION_FAILURE #======================#
    "ZoneValidationException",
]

from system import ValidationException

# ======================# ZONE_VALIDATION_FAILURE #======================#
class ZoneValidationException(ValidationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging
    
    Responsibilities:
        1.  Indicate a Zone validation check was not passed.
        2.  Identify the Validator method where the failure occurred.
    
    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]
    
    Provides:
    
    Super Class:
        TransactionException
    """
    ERR_CODE = "ZONE_VALIDATION_FAILURE"
    MSG = "Failure in ZoneValidator method."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )