# src/command/system/service/operation/build/validation/validator.py

"""
Module: command.root.system.service.operation.build.validation.work
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COMMAND_VALIDATION_FAILURE #======================#
    "CommandValidationException",
]

from system import ValidationException


# ======================# COMMAND_VALIDATION_FAILURE #======================#
class CommandValidationException(ValidationException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Identify which CommandValidator method, a test failed.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super:
        ValidationException
    """
    ERR_CODE = "COMMAND_VALIDATION_FAILURE"
    MSG = "Command validation check failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
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
            title=title,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )