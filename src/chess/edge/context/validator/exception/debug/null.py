# src/chess/rank/validator/exception/null.py

"""
Module: chess.rank.validator.exception.null
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NULL_RANK EXCEPTION #======================#
    "NullRankException",
]

from chess.system import NullException

# ======================# NULL_RANK EXCEPTION #======================#
class NullRankException(NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   Debug

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Null class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    ERR_CODE = "NULL_RANK_EXCEPTION"
    MSG = "Rank validation failed: The candidate cannot be null."
    VAR: None
    VAL = None
    
    _var: Optional[str]
    _val: Optional[None]
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[None] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
        self._var = var
        self._val = val
    
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def val(self) -> Optional[None]:
        return self._val
    
    def __str__(self):
        return f"{super().__str__()}, var:{self._var}, val:{self._val}"
