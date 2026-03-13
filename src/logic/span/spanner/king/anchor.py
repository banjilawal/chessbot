# src/logic/span/spanner/king/anchor.py

"""
Module: logic.span.spanner.king.anchor
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# KING_SPANNER_EXCEPTION #======================#
    "KingSpannerException",
]

from logic.span import SpannerException


# ======================# KING_SPANNER_EXCEPTION #======================#
class KingSpannerException(SpannerException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Provide KingSpanner as:
            *   Reporting
            *   Coverage
        target for layer-2 debugging exceptions.
    2.  Indicate which KingSpanner method received a worker's (layer-1) failure result.

    # PARENT:
        *   SpannerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See SpannerException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SpannerException class for inherited methods.
    """
    CLS_MTHD = Optional[str]
    CLS_NAME = "KingSpanner"
    ERR_CODE = "KING_SPANNER_EXCEPTION"
    MSG = "Exception raised in KingSpanner"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            cls_mthd: Optional[str]
            cls_name: Optional[str
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        
        super().__init__(
            ex=ex, msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )

