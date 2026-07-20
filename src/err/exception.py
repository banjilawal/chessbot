# src/logic/system/err/root.py

"""
Module: logic.system.err.root
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from result import MethodResultType


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
        var: Optional[str]
        val: Optional[Any]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        ex: Optional[Exception]
        mthd_rslt_type: Optional[MethodResultType]
        
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
    _cls_name: Optional[str] | None = None
    _cls_mthd: Optional[str] | None = None
    _ex: Optional[Exception] | None = None
    _mthd_rslt_type: Optional[MethodResultType] | None = None
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: str
            err_code: str
            var: Optional[str]
            val: Optional[Any]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            ex: Optional[Exception]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg)
        self._ex = ex
        self._msg = msg
        self._var = var
        self._val = val
        self._cls_mthd = cls_mthd
        self._cls_name = cls_name
        self._err_code = err_code
        self._mthd_rslt_type = mthd_rslt_type
    
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
    def mthd_rslt_type(self) -> Optional[MethodResultType]:
        return self._mthd_rslt_type
    
    def __str__(self):
        return (
            f"name:{self.__name__}:, "
            f"cls_name:{self._cls_name},"
            f"cls_mthd:{self._cls_mthd},"
            f"errr_code:{self._err_code}, "
            f"msg:{self._msg}, "
            f"mthd_rslt_type:{self._mthd_rslt_type}, "
            f"ex:{self._ex}"
        )




