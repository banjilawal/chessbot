# src/logic/system/collision/exception/validator.py

"""
Module: logic.system.collision.exception.work
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# COLLISION_ANALYST_FAILURE #======================#
    "CollisionAnalystException",
]

from system import OperationException


# ======================# COLLISION_ANALYST_FAILURE #======================#
class CollisionAnalystException(OperationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a CollisionAnalyst exception was aborted because of an error.
        2.  Identify the exception' method where the failure occurred.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]

    Provides:

    Super Class:
        TransactionException
    """
    OP = "CollisionAnalyst"
    MTHD_RSLT = "CollisionAnalystResult"
    ERR_CODE = "COLLISION_ANALYST_FAILURE"
    MSG = "CollisionAnalyst experienced an error. Analyst aborted."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
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
            mthd_rslt=mthd_rslt,
        )
