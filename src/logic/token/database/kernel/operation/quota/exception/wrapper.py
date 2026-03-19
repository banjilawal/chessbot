# src/logic/token/database/kernel/util/quota/exception/worker.py

"""
Module: logic.token.database.kernel.util.quota.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RANK_QUOTA_ANALYZER_FAILURE_EXCEPTION #======================#
    "RankQuotaAnalysisException",
]

from logic.system import AnalysisException


# ======================# RANK_QUOTA_ANALYZER_FAILURE_EXCEPTION #======================#
class RankQuotaAnalysisException(AnalysisException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that  an error prevented a quota analysis from completing.
        2.  Identify the method where the failure occurred.

    Attributes:
        var: Optional[str]
        val: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        err_code: Optional[str]

    Provides:

    Super:
        AnalysisException
    """
    MSG = "Rank quota analysis failed."
    ERR_CODE = "RANK_QUOTA_ANALYZER_FAILURE_EXCEPTION"
    
    def __init__(
            self,
            val: Optional[str] = None,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,

    ):
        """
        Args:
            ex: Optional[str]
            val: Optional[str]
            msg: Optional[str]
            var: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            var=var,
            err_code=err_code,
            val=val,
        )
