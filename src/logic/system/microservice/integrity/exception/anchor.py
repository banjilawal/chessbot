# src/logic/system/microservice/integrity/exception.super.py

"""
Module: logic.system.microservice.integrity.exception.super
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

from logic.system import ServiceException

# ======================# SERVICE_EXCEPTION #======================#
class IntegrityServiceException(ServiceException):
    """
    Role:Debug Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Indicate that an error occurred in an IntegrityMicroService instance.

    Super Class:
    *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityServiceException class for inherited attributes.

    Attributes:
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
    ERR_CODE = "INTEGRITY_SERVICE_EXCEPTION"
    MSG = "IntegrityMicroService raised an exception."
    CLS_NAME = "IntegrityMicroService"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            id: Optional[int] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        super().__init__(
            id=id,
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )