# src/err/analysis/relation/coord/exception.py

"""
Module: err.analysis.relation.coord.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import RelationException

__all__ = [
    # ======================# COORD_RELATION_ERROR #======================#
    "CoordRelationException",
]

# ======================# COORD_RELATION_ERROR #======================#
class CoordRelationException(RelationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a coord relation occurred

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_coord: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]
            
    Provides:

    Super Class:
        RelationException
    """
    MSG = "A coord relation occurred."
    ERR_CODE = "COORD_RELATION_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_coord: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
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
