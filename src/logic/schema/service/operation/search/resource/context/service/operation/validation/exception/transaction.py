# src/logic/schema/database/search/context/service/operation/validation/exception/exception.py

"""
Module: logic.schema.validation.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SCHEMA_CONTEXT_VALIDATION_FAILURE #======================#
    "SchemaContextValidationException",
]

from logic.system import ValidationException


# ======================# SCHEMA_CONTEXT_VALIDATION_FAILURE #======================#
class SchemaContextValidationException(ValidationException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Identify which SchemaContextValidator method, a test failed.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super:
        ValidationException
    """
    MSG = "SchemaContext validation check failed."
    ERR_CODE = "SCHEMA_CONTEXT_VALIDATION_FAILURE"
  
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