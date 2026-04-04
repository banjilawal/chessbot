# src/logic/system/err/root.py

"""
Module: logic.system.err.root
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================#  ROOT APPLICATION EXCEPTION CLASS #======================#
    "ChessException",
]

# ======================# ROOT APPLICATION EXCEPTION CLASS #======================#
class ChessException(Exception):
    """
    Role:Exception

    Responsibilities:
    1.  Parent of exception by the application

    Super Class:
        *   Exception

    Provides:

    # LOCAL ATTRIBUTES:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])

    # INHERITED ATTRIBUTES:
        *   See Exception class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str
        *   ex (Optional[Exception])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See Exception class for inherited methods.
    """
    ERR_CODE = "CHESS_EXCEPTION"
    MSG = "Chess error occurred."
    _msg: str
    _err_code: str
    _var: Optional[str] = None
    _val: Optional[Any] = None
    _cls_name: Optional[str] = None
    _cls_mthd: Optional[str] = None
    _ex: Optional[Exception] = None
    
    
    def __init__(
            self,
            msg=MSG,
            err_code: str = ERR_CODE,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.__class__.__name__
        super().__init__(msg)
        self._ex = ex
        self._msg = msg
        self._var = var
        self._val = val
        self._cls_mthd = cls_mthd
        self._cls_name = cls_name
        self._err_code = err_code
    
    @property
    def ex(self) -> Exception:
        return self._ex
    
    @property
    def err_code(self) -> str:
        return self._err_code
    
    @property
    def msg(self) -> str:
        return self._msg
    
    @property
    def var(self) -> str:
        return self._var
    
    @property
    def val(self) -> str:
        return self._val
    
    @property
    def cls_mthd(self) -> str:
        return self._cls_mthd
    
    @property
    def cls_name(self) -> str:
        return self._cls_name
    
    def __str__(self):
        return (
            f"exception:{self.__name__}:, "
            f"errr_code:{self._err_code}, "
            f"msg:{self._msg}, "
            f"ex:{self._ex}"
            f"cls_name:{self._cls_name}, "
        )




