# src/chess/hostage/service/exception/catchall.py

"""
Module: chess.hostage.service.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""
from typing import Optional

from chess.hostage import HostageException

__all__ = [
    # ======================# HOSTAGE_SERVICE EXCEPTION #======================#
    "HostageServiceException",
]


# ======================# HOSTAGE_SERVICE EXCEPTION #======================#
class HostageServiceException(HostageException, ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for HostageService errors.

    # PARENT:
        *   ServiceException
        *   HostageException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_SERVICE_ERROR"
    MSG = "HostageService raised an exception."
    CLS_NAME = "HostageService"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.CLS_NAME
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name
    
    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}"