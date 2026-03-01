# src/logic/snapshot/service/exception.super.py

"""
Module: logic.snapshot.service.exception.super
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SNAPSHOT_SERVICE_EXCEPTION #======================#
    "SnapshotServiceException",
]

from logic.system import AnchorException

# ======================# SNAPSHOT_SERVICE_EXCEPTION #======================#
class SnapshotServiceException(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a snapshotService.

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
    ERR_CODE = " SNAPSHOT_SERVICE_EXCEPTION"
    MSG = " SnapshotService raised an exception."
    CLS_NAME = " SnapshotService"
    
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