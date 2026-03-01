# src/chess/square/command/command/build/validator/wrapper.py

"""
Module: chess.square.command.command.build.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COMMAND_VALIDATION_FAILURE #======================#
    "CommandValidationException",
]

from chess.system import ValidationException

# ======================# COMMAND_VALIDATION_FAILURE #======================#
class CommandValidationException(ValidationException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identify the CommandValidator method where the process failed.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See ValidationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
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
    ERR_CODE = "COMMAND_VALIDATION_FAILURE"
    MSG = "Failure in CommandValidator method."
    MTHD = None
    OP = "Validate"
    RSLT_TYPE = "ValidationResult"
    
    _op: Optional[str]
    _rslt_type: Optional[str]
    
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