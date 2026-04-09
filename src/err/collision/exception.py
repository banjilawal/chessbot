# src/err/collision/__init__.py

"""
Module: err.collision.__init__
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import ChessException

__all__ = [
    # ======================# COLLISION_FAILURE #======================#
    "CollisionException",
]

# ======================# COLLISION_FAILURE #======================#
class CollisionException(ChessException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that two entities share attribute value that should be unique.
    Attributes:
        op: Optional[str]
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]
            
    Provides:

    Super Class:
        ChessException
    """
    OP = "Collision"
    MSG = str = "Collision step failed."
    ERR_CODE = "COLLISION_FAILURE"
    RSLT_TYPE = "CollisionResult"
    
    _op = Optional[str]
    _rslt_type = Optional[str]
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        op = self.OP
        msg = msg or self.MSG
        rslt_type = self.RSLT_TYPE
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
        self._op = op
        self._rslt_type = rslt_type
    
    @property
    def op(self) -> Optional[str]:
        return self._op
    
    @property
    def rslt_type(self) -> Optional[str]:
        return self._rslt_type
    
    def __str__(self):
        return f"{super().__str__()}, op:{self._op}, rslt_type:{self._rslt_type}"