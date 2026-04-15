# src/err/analysis/collision/context/coord/exception.py

"""
Module: err.analysis.collision.context.coord.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import CollisionException


__all__ = [
    # ======================# COORD_CONTEXT_COLLISION_FAILURE #======================#
    "CoordContextCollisionException",
]

from err import ContextCollisionException


# ======================# COORD_CONTEXT_COLLISION_FAILURE #======================#
class CoordContextCollisionException(ContextCollisionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a CoordContextCollision step failed.

    Attributes:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            
    Provides:

    Super Class:
        ContextCollisionException
    """
    MSG = "No collision logic for CoordContext attribute"
    ERR_CODE = "COORD_CONTEXT_COLLISION_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
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
        )
