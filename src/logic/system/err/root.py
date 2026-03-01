# src/logic/system/err/root.py

"""
Module: logic.system.err.root
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================#  ROOT APPLICATION EXCEPTION CLASS #======================#
    "ChessException",
]

# ======================# ROOT APPLICATION EXCEPTION CLASS #======================#
class ChessException(Exception):
    """
    # ROLE: Exception

    # RESPONSIBILITIES:
    1.  Parent of exception by the application

    # PARENT:
        *   Exception

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])

    # INHERITED ATTRIBUTES:
        *   See Exception class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
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
    
    _err_code: str
    _msg: str
    _ex: Optional[Exception]
    
    def __init__(
            self,
            err_code: str = ERR_CODE,
            msg: str = MSG,
            ex: Optional[Exception] = None
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        
        super().__init__(msg)
        self._ex = ex
        self._msg = msg
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
    
    def __str__(self):
        return f"exception:{self.__name__}:, errr_code:{self._err_code}, msg:{self._msg}, ex:{self._ex}"




