# src/logic/square/service/visitation/exception/terminate/validator.py

"""
Module: logic.square.service.visitation.exception.terminate.work
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_VISIT_TERMINATION_FAILURE #======================#
    "SquareDepartureException",
]

from system import DeletionException

# ======================# SQUARE_VISIT_TERMINATION_FAILURE #======================#
class SquareDepartureException(DeletionException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a SquareDepartureProcess was not completed.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
        
    Provides:
    
    Super Class:
         DeletionException
    """
    OP = "Delete"
    MTHD_RSLT = "DeletionResult"
    MSG = "Square visit termination failed."
    ERR_CODE = "SQUARE_VISIT_TERMINATION_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
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
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )
