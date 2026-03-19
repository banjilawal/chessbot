# src/logic/square/database/kernel/util/quota/exception/work.py

"""
Module: logic.square.database.kernel.util.quota.exception.work
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RANK_QUOTA_ANALYSIS_FAILURE #======================#
    "SquareStackAnalysisException",
]

from logic.system import AnalysisException


# ======================# RANK_QUOTA_ANALYSIS_FAILURE #======================#
class SquareStackAnalysisException(AnalysisException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that  an error prevented a quota analysis from completing.
        2.  Identify the method where the failure occurred.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super:
        AnalysisException
    """
    OP = "Computation"
    RSLT_TYPE = "ComputationResult"
    MSG = "Rank quota analysis failed."
    ERR_CODE = "RANK_QUOTA_ANALYSIS_FAILURE"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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
            err_code=err_code,
            rslt_type=rslt_type,
        )
