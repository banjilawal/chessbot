# src/logic/span/spanner/bishop/service/exception/anchor.py

"""
Module: logic.span.spanner.bishop.service.exception.anchor
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

from logic.span import SpanServiceException

# ======================# BISHOP_SPAN_SERVICE_EXCEPTION #======================#
class BishopSpanServiceException(SpanServiceException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a BishopSpanService.

    # PARENT:
    *   SpanServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See SpanServiceException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SpanServiceException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "BishopSpanService"
    ERR_CODE = "BISHOP_SPAN_SERVICE_EXCEPTION"
    MSG = " BishopSpanService raised an exception."
  
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
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