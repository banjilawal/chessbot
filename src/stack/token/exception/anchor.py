# src/logic/token/database/kernel/exception/anchor.py

"""
Module: logic.token.database.kernel.exception.anchor
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_STACK_SERVICE_EXCEPTION #======================#
    "TokenStackServiceException",
]

from system import StackServiceException


# ======================# TOKEN_STACK_SERVICE_EXCEPTION #======================#
class TokenStackServiceException(StackServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors TokenStackService debug (layer-2) information.
        2.  Indicate which TokenStackService method received a  worker's (layer-1)
            failure result.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:

    Super Class:
        StackServiceException
    """
    CLS_NAME = "TokenStackService"
    ERR_CODE = "TOKEN_STACK_SERVICE_EXCEPTION"
    MSG = "TokenStackService raised an exception."
    
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
        super().__init__(
            ex=ex,
            msg=msg,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            err_code=err_code,
        )
