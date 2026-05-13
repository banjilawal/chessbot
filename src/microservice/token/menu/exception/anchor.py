# src/logic/token/service/menu/exception/anchor.py

"""
Module: logic.token.service.menu.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_SERVICE_MENU_EXCEPTION #======================#
    "TokenServiceMenuException",
]

from system import AnchorException


# ======================# TOKEN_SERVICE_MENU_EXCEPTION #======================#
class TokenServiceMenuException(AnchorException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors TokenServiceMenu debug (layer-2) information.
        2.  Indicate which TokenServiceMenu method received a worker's (layer-1) failure result.

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
    ERR_CODE = "TOKEN_SERVICE_MENU_EXCEPTION"
    MSG = "TokenServiceMenu raised an exception."
    
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
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
