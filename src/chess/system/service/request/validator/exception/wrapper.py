# src/chess/system/service/request/validator/wrapper.py

"""
Module: chess.system.service.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from typing import Optional

from chess.system import ValidationException

__all__ = [
    # ======================# SERVICE_REQUEST_VALIDATION_FAILURE #======================#
    "ServiceRequestValidationException",
]

# ======================# SERVICE_REQUEST_VALIDATION_FAILURE #======================#
class ServiceRequestValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that An error occurred in ServiceRequestValidator.validator.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ServiceRequest.validate error."
    MSG = "An exception was raised in ServiceRequestValidator.validator."
    CLS_NAME = "ServiceRequestValidator"
    
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
    
    