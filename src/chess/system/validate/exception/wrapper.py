# src/chess/system/validate/exception/wrapper.py

"""
Module: chess.system.validate.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import Optional

from chess.system import OperationException

__all__ = [
    # ======================# VALIDATION_FAILURE #======================#
    "ValidationException",
]


#======================# VALIDATION_FAILURE #======================#
class ValidationException(OperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes which check the candidate failed.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VALIDATION_FAILURE"
    MSG = "Validation failed."
    MTHD: "validate"
    OP_NAME = "validate"
    RSLT = "ValidationResult"
    
    
    def __init__(
            self,
            op_name: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd = mthd or self.MTHD
        op_name = op_name or self.OP_NAME
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._mthd = mthd
        self._op_name = op_name or self.OP_NAME
    
    @property
    def op_name(self) -> Optional[str]:
        return self._op_name
    
    def __str__(self):
        return f"{super().__str__()}, op_name:{self._op_name}"