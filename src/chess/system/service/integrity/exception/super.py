# src/chess/system/service/integrity/exception.super.py

"""
Module: chess.system.service.integrity.exception.super
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_EXCEPTION #======================#
    "IntegrityServiceException",
]

from chess.system import ServiceException

# ======================# SERVICE_EXCEPTION #======================#
class IntegrityServiceException(ServiceException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in an IntegrityService instance..

    # PARENT:
    *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See IntegrityServiceException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   id (Optional[int])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ServiceException class for inherited methods.
    """
    ERR_CODE = "ENTITY_SERVICE_ERROR"
    MSG = "IntegrityService raised an exception."
    CLS_NAME = "IntegrityService"
    
    _cls_name: Optional[str]
    _id: Optional[int]
    
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