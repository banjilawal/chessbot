# src/logic/team/service/operation/validation/exception/work.py

"""
Module: logic.team.service.operation.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TEAM_VALIDATION_FAILURE #======================#
    "TeamValidationException",
]

from logic.system import ValidationException


# ======================# TEAM_VALIDATION_FAILURE #======================#
class TeamValidationException(ValidationException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the TeamValidationTransaction method where the exception failed.

    Super Class:
        *   ValidationException

    Provides:

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

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
    ERR_CODE = "TEAM_VALIDATION_FAILURE"
    MSG = "Failure in TeamValidationTransaction method."
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    
    _op = Optional[str]
    _rslt_type = Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
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