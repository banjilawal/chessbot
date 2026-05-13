# src/err/analysis/relation/team/binder/exception.py

"""
Module: err.analysis.relation.team.binder.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# BINDER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
    "BinderTeamAnalysisException",
]

from err.analysis.relation import RelationException


# ======================# BINDER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
class BinderTeamAnalysisException(RelationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error prevented a BinderTeamRelations analysis from completing.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        IdRelationException
    """
    MSG = "A BinderTeamRelations analysis step failed."
    ERR_CODE = "BINDER_TEAM_RELATION_ANALYSIS_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
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
