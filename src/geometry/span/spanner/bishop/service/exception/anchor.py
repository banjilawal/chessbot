# src/geometry/span/spanner/bishop/service/exception/anchor.py

"""
Module: geometry.span.spanner.bishop.service.exception.anchor
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# BISHOP_SPAN_SERVICE_EXCEPTION #======================#
    "BishopSpanServiceException",
]

from math.span import SpanServiceException

# ======================# BISHOP_SPAN_SERVICE_EXCEPTION #======================#
class BishopSpanServiceException(SpanServiceException):
    """
    Role:Debug Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Indicate that an error occurred in a BishopSpanService.

    Super Class:
    *   SpanServiceException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See SpanServiceException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SpanServiceException class for inherited methods.
    """
    CLS_MTHD = Optional[str]
    CLS_NAME = "BishopSpanService"
    ERR_CODE = "BISHOP_SPAN_SERVICE_EXCEPTION"
    MSG = "BishopSpanService raised an exception."
  
    def __init__(
            self,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)