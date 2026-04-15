# src/logic/token/service/operation/promotion/exception/validator.py

"""
Module: logic.token.service.operation.promotion.exception.work
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAWN_PROMOTION_FAILURE #======================#
    "PromotionException",
]

from system import UpdateException

# ======================# PAWN_PROMOTION_FAILURE #======================#
class PromotionException(UpdateException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that promoting a pawn_token failed.
        2.  Identify the PawnPromoter method where the failure occurred.
    
    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]
        
    Provides:

    Super Class:
        TokenDebugException
    """
    OP = "PawnPromoter"
    RSLT_TYPE = "UpdateResult"
    ERR_CODE = "PAWN_PROMOTION_FAILURE"
    MSG = "PawnPromoter method failed."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[ResultCategory]
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