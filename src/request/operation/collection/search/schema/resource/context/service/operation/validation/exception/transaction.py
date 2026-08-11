# src/logic/schema/database/searcher/context/service/operation/validation/exception/exception.py

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
    "SchemaContextValidatorException",
]

from system import ValidatorException


# ======================# SCHEMA_CONTEXT_VALIDATION_FAILURE #======================#
class SchemaContextValidatorException(ValidatorException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Identify which SchemaContextValidator method, a test failed.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super:
        ValidatorException
    """
    MSG = "SchemaContext validation check failed."
    ERR_CODE = "SCHEMA_CONTEXT_VALIDATION_FAILURE"
  
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
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