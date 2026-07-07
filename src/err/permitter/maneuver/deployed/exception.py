# src/err/permitter/maneuver/deployed/exception.py

"""
Module: err.permitter.maneuver.deployed.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import TokenUndoMovePermitterException
from result import MethodResultType

__all__ = [
    # ======================# MOVE_UNDEPLOYED_TOKEN_ERROR #======================#
    "MoveUndeployedTokenException",
]

# ======================# MOVE_UNDEPLOYED_TOKEN_ERROR #======================#
class MoveUndeployedTokenException(TokenUndoMovePermitterException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an attempt was made to move a token which has not
            been deployed to its home square.
            
    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        Mthd_Rslt_Type: Optional[MethodResultType]
        
    Provides:

    Super Class:
        TokenUndoMovePermitterException
    """
    MSG = "Cannot move a token until its placed on its home square first."
    ERR_CODE = "MOVE_UNDEPLOYED_TOKEN_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: Optional[Exception]
            cls_name: Optional[Str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt_type=mthd_rslt_type,
        )