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
    # ======================# SCHEMA_QUERY_BUILD_FAILURE #======================#
    "SchemaQueryBuildException",
]

from system import BuildException


# ======================# SCHEMA_QUERY_BUILD_FAILURE #======================#
class SchemaQueryBuildException(BuildException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that, an error prevented a SchemaCQuery from being built.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super Class:
        BuildException
    """
    MSG = "A SchemaQueryBuilder method failed."
    ERR_CODE = "SCHEMA_QUERY_BUILD_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd_rslt_type: Optional[MethodResultType] = None,
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