# src/chess/system/service/root/exception.py

"""
Module: chess.system.service.root.exception
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations
from typing import Optional

from chess.system import SuperClassException

__all__ = [
    # ======================# SERVICE EXCEPTION #======================#
    "ServiceException",
]


# ======================# SERVICE EXCEPTION #======================#
class ServiceException(SuperClassException):
    """
    # ROLE: Super, Exception Messaging
    
    # RESPONSIBILITIES:
    1. Outermost layer of the 3-part exception chain that is created when a Service operation's crashes.

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_ERROR"
    MSG = "Service raised an exception."
    CLS_NAME = "Service"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        super().__init__(ex=ex, err_code=err_code, msg=msg, cls_name=cls_name)
