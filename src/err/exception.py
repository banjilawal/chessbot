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
    Role:
        -   Exception

    Responsibilities:
        1.  Parent of exceptions in the application.
        
    Attributes:
        msg: str
        err_code: str
        op: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        ex: Optional[Exception]
        rslt_type: Optional[str]
        
    Provides:
    
    Super Class:
        Exception
    """
    ERR_CODE = "CHESS_EXCEPTION"
    MSG = "Chess error occurred."
    
    _msg: str
    _err_code: str
    _var: Optional[str] | None = None
    _val: Optional[Any] | None = None
    _op: Optional[Any] | None = None
    _rslt_type: Optional[str] | None = None
    _cls_name: Optional[str] | None = None
    _cls_mthd: Optional[str] | None = None
    _ex: Optional[Exception] | None = None
    
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            op: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            rslt_type: Optional[str] | None = None,
    ):
        """
        Args:
            msg: str
            err_code: str
            op: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            ex: Optional[Exception]
            rslt_type: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.__class__.__name__
        super().__init__(msg)
        self._op = op
        self._ex = ex
        self._msg = msg
        self._var = var
        self._val = val
        self._cls_mthd = cls_mthd
        self._cls_name = cls_name
        self._err_code = err_code
        self._rslt_type = rslt_type
        
    @property
    def op(self) -> Optional[str]:
        return self._op
    
    @property
    def ex(self) -> Optional[Exception]:
        return self._ex
    
    @property
    def err_code(self) -> str:
        return self._err_code
    
    @property
    def msg(self) -> str:
        return self._msg
    
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def val(self) -> Optional[str]:
        return self._val
    
    @property
    def cls_mthd(self) -> Optional[str]:
        return self._cls_mthd
    
    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    @property
    def rslt_type(self) -> Optional[str]:
        return self._rslt_type
    
    def __str__(self):
        return (
            f"exception:{self.__name__}:, "
            f"errr_code:{self._err_code}, "
            f"msg:{self._msg}, "
            f"ex:{self._ex}"
            f"cls_name:{self._cls_name}, "
        )




