# src/logic/token/database/search/context/service/operation/build/exception/transaction.py

"""
Module: logic.token.database.search.context.service.operation.build.exception.transaction
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_QUERY_BUILD_FAILURE #======================#
    "TokenQueryBuildException",
]

from system import BuildException


# ======================# TOKEN_QUERY_BUILD_FAILURE #======================#
class TokenQueryBuildException(BuildException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that, an error prevented a TokenCQuery from being built.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[resultCategory]

    Provides:

    Super Class:
        BuildException
    """
    MSG = "A TokenQueryBuilder method failed."
    ERR_CODE = "TOKEN_QUERY_BUILD_FAILURE"
    
    def __init__(
            self, = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[resultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[resultCategory]
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