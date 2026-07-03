# src/logic/schema/database/search/context/service/operation/build/exception/transaction.py

"""
Module: logic.schema.database.search.context.service.operation.build.exception.transaction
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# SCHEMA_CONTEXT_BUILDER_FAILURE #======================#
    "SchemaContextBuilderException",
]

from system import BuilderException


# ======================# SCHEMA_CONTEXT_BUILDER_FAILURE #======================#
class SchemaContextBuilderException(BuilderException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that, an error prevented a SchemaContext from being built.
        2.  Trace the method calls.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super:
        BuilderException
    """
    ERR_CODE = "SCHEMA_CONTEXT_BUILDER_FAILURE"
    MSG = "A SchemaContextBuilder method failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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