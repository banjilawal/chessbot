# src/chess/system/service/exception.super.py

"""
Module: chess.system.service.exception.super
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_EXCEPTION #======================#
    "ServiceException",
]

from chess.system import SuperClassException

# ======================# SERVICE_EXCEPTION #======================#
class ServiceException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a Service.

    # PARENT:
    *   SuperClassException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See SuperClassException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SuperClassException class for inherited methods.
    """
    ERR_CODE = "SERVICE_EXCEPTION"
    MSG = " Service raised an exception."
    CLS_NAME = "Service"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name)