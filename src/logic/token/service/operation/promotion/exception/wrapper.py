# src/logic/token/service/operation/promotion/exception/worker.py

"""
Module: logic.token.service.operation.promotion.exception.wrapper
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAWN_PROMOTION_FAILURE #======================#
    "PromotionProcessException",
]

from logic.system import UpdateException

# ======================# PAWN_PROMOTION_FAILURE #======================#
class PromotionProcessException(UpdateException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that promoting a pawn_token failed.
        2.  Identify the PawnPromotionProcess method where the failure occurred.
    
    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]
        
    Provides:

    Super Class:
        TokenDebugException
    """
    OP = "PawnPromotionProcess"
    RSLT_TYPE = "UpdateResult"
    ERR_CODE = "PAWN_PROMOTION_FAILURE"
    MSG = "PawnPromotionProcess method failed."
    
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