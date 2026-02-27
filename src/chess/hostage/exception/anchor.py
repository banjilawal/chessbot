# src/chess/hostage/exception/debug.py

"""
Module: chess.hostage.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# HOSTAGE_EXCEPTION #======================#
    "HostageException",
]

from chess.system import AnchorException

# ======================# HOSTAGE_EXCEPTION #======================#
class HostageException(AnchorException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Provide Hostage as:
            *   Reporting
            *   Coverage
        target for layer-2 debugging exceptions.
    2.  Indicate which Hostage method received a worker's (layer-1) failure result.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])
        
    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    ERR_CODE = "HOSTAGE_EXCEPTION"
    MSG = "Exception raised in Hostage"
    CLS_NAME = "Hostage"
    CLS_MTHD = None
 
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
        cls_mthd = cls_mthd or self.CLS_MTHD
        
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )
