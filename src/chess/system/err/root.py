# src/chess/system/err/base.py

"""
Module: chess.system.err.base
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from typing import Optional

__all__ = [
    # ======================#  BASE APPLICATION EXCEPTION CLASS #======================#
    "ChessException",
]


# ======================# BASE APPLICATION EXCEPTION CLASS #======================#
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
    None

    # INHERITED ATTRIBUTES:
        *   See Exception class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See Exception class for inherited methods.
    """
    ERR_CODE = "CHESS_ERROR"
    MSG = "Chess error occurred."
    
    _msg: str
    _err_code: str
    _ex: Optional[Exception]
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            ex: Optional[Exception] = None
    ):
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
        return f"exception:{self.__name__}:, errr_code:{self._err_code}, msg:{self._msg}"
    
    # Only the super class needs the explict constructor
    # def __init__(self, msg: str):
    #     self.msg = msg or self.MSG
    #     super().__init__(self.msg)
    
    # Only the super class needs to declare team_name toString. Subclasses
    # will use this.




