# src/logic/token/database/search/service/exception/anchor.py

"""
Module: logic.token.database.search.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_SEARCH_SERVICE_FAILURE #======================#
    "TokenSearchServiceException",
]

from system import ServiceException

# ======================# TOKEN_SEARCH_SERVICE_FAILURE #======================#
class TokenSearchServiceException(ServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors TokenSearchService debug (layer-2) information.
        2.  Indicate which TokenSearchService method received a worker's
            (layer-1) failure result.


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
    CLS_NAME = "TokenSearchService"
    ERR_CODE = "TOKEN_SEARCH_SERVICE_FAILURE"
    MSG = "TokenSearchService raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
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
