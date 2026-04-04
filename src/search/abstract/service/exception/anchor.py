# src/logic/system/search/service/exception/anchor.py

"""
Module: logic.system.search.service.exception.anchor
Author: Banji Lawal
Created: 2026-03-31
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SEARCH_SERVICE_EXCEPTION #======================#
    "SearchServiceException",
]

from system import ServiceException


# ======================# SEARCH_SERVICE_EXCEPTION #======================#
class SearchServiceException(ServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors SearchService debug (layer-2) information.
        2.  Indicate which SearchService method received a worker's (layer-1) failure result.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:

    Super Class:
        ServiceException
    """
    ERR_CODE = "SEARCH_SERVICE_EXCEPTION"
    MSG = "SearchService raised an exception."
    
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
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
