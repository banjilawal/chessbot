# src/logic/system/collision/exception/work.py

"""
Module: logic.system.collision.exception.work
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# COLLISION_ANALYSIS_FAILURE #======================#
    "CollisionAnalysisException",
]

from logic.system import OperationException


# ======================# COLLISION_ANALYSIS_FAILURE #======================#
class CollisionAnalysisException(OperationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a CollisionAnalysis exception was aborted because of an error.
        2.  Identify the exception' method where the failure occurred.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super Class:
        OperationException
    """
    OP = "CollisionAnalysis"
    RSLT_TYPE = "CollisionAnalysisResult"
    ERR_CODE = "COLLISION_ANALYSIS_FAILURE"
    MSG = "CollisionAnalysis experienced an error. Analysis aborted."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
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
