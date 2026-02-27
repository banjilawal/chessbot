# src/chess/system/err/anchor/root.py

"""
Module: chess.system.err.anchor.root
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ANCHOR_EXCEPTION #======================#
    "AnchorException",
]

from chess.system import ChessException


# ======================# ANCHOR_EXCEPTION #======================#
class AnchorException(ChessException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Reporting and coverage target for Anchor DebugExceptions.
    2.  Indicate which Anchor method received a worker's failure result.

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
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "ANCHOR_EXCEPTION"
    MSG = "Exception raised in Anchor"
    CLS_NAME = "Anchor"
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