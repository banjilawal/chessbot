# src/logic/system/relation/exception/validator.py

"""
Module: logic.system.relation.exception.work
Author: Banji Lawal
Created: 2026-01-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RELATION_ANALYST_FAILURE #======================#
    "RelationAnalystException",
]

from system import OperationException


# ======================# RELATION_ANALYST_FAILURE #======================#
class RelationAnalystException(OperationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a RelationAnalyst exception was aborted because of an error.
        2.  Identify the exception' method where the failure occurred.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super Class:
        TransactionException
    """
    OP = "RelationAnalyst"
    MTHD_RSLT = "RelationAnalystResult"
    ERR_CODE = "RELATION_ANALYST_FAILURE"
    MSG = "RelationAnalyst experienced an error. Analyst aborted."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
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



    

