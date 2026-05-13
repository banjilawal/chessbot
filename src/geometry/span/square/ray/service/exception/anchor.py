# src/geometry/span/square/ray/service/exception.anchor.py

"""
Module: geometry.span.square.ray.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_RAY_SERVICE_EXCEPTION #======================#
    "SquareRayServiceException",
]

from system import AnchorException

# ======================# SQUARE_RAY_SERVICE_EXCEPTION #======================#
class SquareRayServiceException(AnchorException):
    """
    Role:Debug Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Indicate that an error occurred in a SquareRayService.

    Super Class:
    *   AnchorException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_MTHD = Optional[str]
    CLS_NAME = "SquareRayService"
    ERR_CODE = "SQUARE_RAY_SERVICE_EXCEPTION"
    MSG = "SquareRayService raised an exception."
  
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