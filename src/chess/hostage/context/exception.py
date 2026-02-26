# src/chess/hostage/context/exception.py

"""
Module: chess.hostage.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""
from typing import Optional

from chess.hostage import HostageException
from chess.system import ContextException

__all__ = [
    # ======================# HOSTAGE_CONTEXT EXCEPTION #======================#
    "CaptivityContextException",
]


# ======================# HOSTAGE_CONTEXT EXCEPTION #======================#
class CaptivityContextException(HostageException, ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CaptivityContext objects.

    # PARENT:
        *   HostageException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_CONTEXT_ERROR"
    DEFAULT_ERR_CODE = "HostageContext raised an exception."
    CLS_NAME = "HostageContext"
    
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