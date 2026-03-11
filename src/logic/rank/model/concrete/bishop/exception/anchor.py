# src/logic/rank/model/concrete/bishop/exception/anchor.py

"""
Module: logic.rank.model.concrete.bishop.exception.anchor
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# BISHOP_EXCEPTION #======================#
    "BishopException",
]


# ======================# BISHOP_EXCEPTION #======================#
class BishopException(RankException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Provide Rank as:
            *   Reporting
            *   Coverage
        target for layer-2 debugging exceptions.
    2.  Indicate which Bishop method received a worker's (layer-1) failure result.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See RankException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See RankException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "Bishop"
    ERR_CODE = "BISHOP_EXCEPTION"
    MSG = "Exception raised in Bishop"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            cls_mthd: Optional[str]
            cls_name: Optional[str
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        
        super().__init__(
            ex=ex, msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )

