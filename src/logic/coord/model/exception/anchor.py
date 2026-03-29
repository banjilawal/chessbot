# src/logic/coord/model/exception/anchor.py

"""
Module: logic.coord.model.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_EXCEPTION #======================#
    "CoordException",
]

from logic.system import AnchorException


# ======================# COORD_EXCEPTION #======================#
class CoordException(AnchorException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchoring target for Coord debug (layer-2) error variable information.
        2.  Indicate which Coord method received a worker's (layer-1) failure result.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:

    Super Class:
        AnchorException
    """
    CLS_NAME = "Coord"
    ERR_CODE = "COORD_EXCEPTION"
    MSG = "Coord raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
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
        cls_name = cls_name or self.CLS_NAME
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)
