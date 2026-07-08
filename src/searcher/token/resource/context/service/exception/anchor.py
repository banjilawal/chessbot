# src/logic/token/database/searcher/context/service/exception/anchor.py

"""
Module: logic.token.database.searcher.context.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_CONTEXT_SERVICE_EXCEPTION #======================#
    "TokenContextServiceException",
]

from system import ServiceException


# ======================# TOKEN_CONTEXT_SERVICE_EXCEPTION #======================#
class TokenContextServiceException(ServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors TokenContextService debug (layer-2) information.
        2.  Indicate which TokenContextService method received a  worker's (layer-1)
            failure result.

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
    ERR_CODE = "TOKEN_CONTEXT_SERVICE_EXCEPTION"
    MSG = "TokenContextService raised an exception."
    
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
        super().__init__(
            ex=ex,
            msg=msg,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            err_code=err_code,
        )