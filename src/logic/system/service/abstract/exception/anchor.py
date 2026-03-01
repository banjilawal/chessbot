# src/logic/system/service/abstract/exception.anchor.py

"""
Module: logic.system.service.abstract.exception.anchor
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

from logic.system import AnchorException

# ======================# SERVICE_EXCEPTION #======================#
class ServiceException(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Reporting and coverage for Service DebugExceptions.
    2.  Uses cls_mthd attribute to show which Service method received a failure
        result from a worker.

    # PARENT:
    *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   _id (int)

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])
        *   id (Optional[int])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    ERR_CODE = "SERVICE_EXCEPTION"
    MSG = " Service raised an exception."
    CLS_NAME = "Service"
    
    _cls_name:str = None
    _id: int = None
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            id: Optional[int] = None,
    ):
        self._id = id
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )
        self._id = id
        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    def __str__(self) -> str:
        return f"{super().__str__()}, id:{self._id}"