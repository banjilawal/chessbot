# src/command/request/exception/anchor.py

"""
Module: command.request.exception.anchor
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# SERVICE_REQUEST_EXCEPTION #======================#
    "RequestException",
]

from typing import Optional
from chess.system import AnchorException


# ======================# SERVICE_REQUEST_EXCEPTION #======================#
class RequestException(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of RequestDebugException

    # PARENT:
      *   AnchorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_REQUEST_EXCEPTION"
    MSG = "Request raised an exception."
    CLS_NAME = "Request"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )