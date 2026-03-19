# src/logic/square/service/visitation/exception/terminate/wrapper.py

"""
Module: logic.square.service.visitation.exception.terminate.wrapper
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

from logic.system import DeletionException

# ======================# SQUARE_VISIT_TERMINATION_FAILURE #======================#
class SquareDepartureException(DeletionException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a SquareDepartureProcess was not completed.
        2.  Identify the method where the failure occurred.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]
        
    Provides:
    
    Super Class:
         DeletionException
    """
    OP = "Delete"
    RSLT_TYPE = "DeletionResult"
    MSG = "Square visit termination failed."
    ERR_CODE = "SQUARE_VISIT_TERMINATION_FAILURE"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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
            err_code=err_code,
            rslt_type=rslt_type,
        )
