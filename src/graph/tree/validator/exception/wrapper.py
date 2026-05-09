# src/logic/pair/tree/validation/exception/validator.py

"""
Module: logic.pair.tree.validation.exception.work
Author: Banji Lawal
Created: 2026-03-12
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_TREE_VALIDATION_FAILURE #======================#
    "NodeTreeValidationException",
]

from system import ValidationException

# ======================# NODE_TREE_VALIDATION_FAILURE #======================#
class NodeTreeValidationException(ValidationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the NodeTreeValidator method where the exception failed.

    Super Class:
        *   ValidationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ValidationException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ValidationException class for inherited methods.
    """
    MTHD_RSLT = "ValidationResult"
    ERR_CODE = "NODE_TREE_VALIDATION_FAILURE"
    MSG = "Failure in NodeTreeValidator method."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd_rslt_type: Optional[MethodResultType] = None,
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