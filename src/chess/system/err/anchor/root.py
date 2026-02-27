# src/chess/system/err/super.py

"""
Module: chess.system.err.super
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# CLASS_EXCEPTION #======================#
    "AnchorException",
]

from chess.system import ChessException


# ======================# CLASS_EXCEPTION #======================#
class AnchorException(ChessException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  DebugExceptions use an AnchorException as a point of focus for
        on which object they cover.

    # NAMING CONVENTION:
    1.  Class name followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class name followed by the ERROR suffix.
    2.  The Syntax is: [Class]_EXCEPTION

    # DEFAULT MSG CONVENTION:
    1.  Class name followed by "raised an exception."
    2.  The Syntax is: [Class] raised an exception

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])
        
    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See Exception class for inherited methods.
    """
    ERR_CODE = "CLASS_EXCEPTION"
    MSG = "Class exception was raised."
    CLS_NAME = "Class"
    CLS_MTHD = None

    _cls_name: Optional[str]
    _cls_mthd: Optional[str]
 
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD

        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name
        _cls_mthd = cls_mthd

    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    @property
    def cls_mthd(self) -> Optional[str]:
        return self._cls_mthd
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}, cls_mthd:{self._cls_mthd}"