# src/command/request/validation/validator.py

"""
Module: command.request.validation.work
Author: Banji Lawal
Created: 2026-02-24
"""


from __future__ import annotations
from typing import Optional

from system import ValidationException

__all__ = [
    # ======================# ARGUMENTS_VALIDATION_FAILURE #======================#
    "ArgumentsValidationException",
]

# ======================# ARGUMENTS_VALIDATION_FAILURE #======================#
class ArgumentsValidationException(ValidationException):
    """
    Role:Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that a rank failed a safety check in a CommandArgsValidator
        method.

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
    ERR_CODE = "ARGUMENTS_VALIDATION_FAILURE"
    MSG = "Arguments validation test failed."
    MTHD = "validate"
    MTHD_RSLT = "ValidationResult"
    
    def __init__(
            self,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd: Optional[str] = None, = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, mthd_rslt_type=mthd_rslt_type)
    
    