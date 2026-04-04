# src/logic/system/err/anchor/root.py

"""
Module: logic.system.err.anchor.root
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from err import ChessException

__all__ = [
    # ======================# ANCHOR_EXCEPTION #======================#
    "AnchorException",
]

# ======================# ANCHOR_EXCEPTION #======================#
class AnchorException(ChessException):
    """
    Role:Coverage Target, Exception Chain Layer 0

    Responsibilities:.
    1.  Anchors debug (layer-2) error state firing incident reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which Anchor method received a worker's (layer-1) failure result.

    # NAMING CONVENTION:
    1.  Class schema followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class schema followed by the ERROR suffix.
    2.  The Syntax is: [Class]_EXCEPTION

    # DEFAULT MSG CONVENTION:
    1.  Class schema followed by "raised an exception."
    2.  The Syntax is: [Class] raised an exception

    Super Class:
        *   ChessException

    Provides:

    # LOCAL ATTRIBUTES:
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        
    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        err_code: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    CLS_NAME = "Anchor"
    ERR_CODE = "ANCHOR_EXCEPTION"
    MSG = "Exception raised in Anchor"

    _var: Optional[str]
    _val: Optional[Any]
    _cls_name: Optional[str]
    _cls_mthd: Optional[str]
 
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None
    ):
        """
        Args:
            msg: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
        """
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        err_code = err_code or self.ERR_CODE

        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _var = var
        _val = val
        _cls_name = cls_name
        _cls_mthd = cls_mthd
        
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def val(self) -> Optional[Any]:
        return self._val

    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    @property
    def cls_mthd(self) -> Optional[str]:
        return self._cls_mthd
    
    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"var:{self._var}:, "
            f"cls_name:{self._cls_name}, "
            f"cls_mthd:{self._cls_mthd}"
        )