# src/logic/token/service/operation/promotion/exception/wrapper.py

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
    "PromotionException",
]

from logic.system import UpdateException

# ======================# PAWN_PROMOTION_FAILURE #======================#
class PromotionException(UpdateException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that promoting a pawn_token failed.
    2.  Identify the PawnPromotion method where the failure occurred.

    # PARENT:
        UpdateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UpdateException class for inherited attributes.

    # CONSTRUCTOR:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See UpdateException class for inherited methods.
    """
    OP = "PawnPromotion"
    RSLT_TYPE = "UpdateResult"
    ERR_CODE = "PAWN_PROMOTION_FAILURE"
    MSG = "PawnPromotion method failed."
    
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
        mthd = mthd or self.MTHD
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