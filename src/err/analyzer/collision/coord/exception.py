# src/err/analyzer/collision/coord/exception.py

"""
Module: err.analyzer.collision.coord.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import CollisionException

__all__ = [
    # ======================# COORD_COLLISION_ERROR #======================#
    "CoordCollisionException",
]

# ======================# COORD_COLLISION_ERROR #======================#
class CoordCollisionException(CollisionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a coord collision occurred

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_coord: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        CollisionException
    """
    MSG = "A coord collision occurred."
    ERR_CODE = "COORD_COLLISION_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_coord: Optional[str] = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_coord: Optional[str]
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
            cls_coord=cls_coord,
            cls_mthd=cls_mthd,
        )
