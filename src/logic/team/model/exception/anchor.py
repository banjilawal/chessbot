# src/logic/team/model/exception/anchor.py

"""
Module: logic.team.model.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TEAM_EXCEPTION #======================#
    "TeamException",
]

from logic.system import AnchorException


# ======================# TEAM_EXCEPTION #======================#
class TeamException(AnchorException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchoring target for Team debug exceptions.
        2.  Indicate which Team method received a worker's (layer-1) failure result.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:
    
    Super Class:
        AnchorException
    """
    CLS_NAME = "Team"
    ERR_CODE = "TEAM_EXCEPTION"
    MSG = "Team raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)
