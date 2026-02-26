# src/chess/node/validator/exception/wrapper.py

"""
Module: chess.node.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.system import ValidationException

__all__ = [
    # ======================# NODE_VALIDATION_FAILURE #======================#
    "NodeValidationException",
]

# ======================# NODE_VALIDATION_FAILURE #======================#
class NodeValidationException(ValidationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed a safety check in a NodeValidator method.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

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
    ERR_CODE = "NODE_NODE_VALIDATION_FAILURE"
    MSG = "Safety check failed.."
    MTHD = "validate"
    OP = "Validation"
    RSLT_TYPE = "ValidationResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)

