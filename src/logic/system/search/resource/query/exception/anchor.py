# src/logic/system/search/resource/context/exception/anchor.py

"""
Module: logic.system.search.resource.context.exception.anchor
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# QUERY_EXCEPTION #======================#
    "QueryException",
]

from logic.system import AnchorException


# ======================# QUERY_EXCEPTION #======================#
class QueryException(AnchorException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors Query debug (layer-2) information.
        2.  Indicate which Query method received a worker's (layer-1)
            failure result.

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
    ERR_CODE = "QUERY_EXCEPTION"
    MSG = "Query raised an exception."
    
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
