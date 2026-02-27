# src/chess/hostage/service/exception.super.py

"""
Module: chess.hostage.service.exception.super
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# HOSTAGE_SERVICE_EXCEPTION #======================#
    "HostageServiceException",
]

from chess.system import AnchorException

# ======================# HOSTAGE_SERVICE_EXCEPTION #======================#
class HostageServiceException(AnchorException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a hostageService.

    # PARENT:
    *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    ERR_CODE = " HOSTAGE_SERVICE_EXCEPTION"
    MSG = " HostageService raised an exception."
    CLS_NAME = " HostageService"
    
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