# src/logic/coord/context/exception/anchor.py

"""
Module: logic.coord.context.exception.anchor
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_CONTEXT_EXCEPTION #======================#
    "CoordContextException",
]

from logic.system import AnchorException


# ======================# COORD_CONTEXT_EXCEPTION #======================#
class CoordContextException(AnchorException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Anchoring target for CoordContext debug (layer-2) error state firing incident
        reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which CoordContext method received a worker's (layer-1) failure result.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_NAME = " CoordContext"
    ERR_CODE = " COORD_CONTEXT_EXCEPTION"
    MSG = " CoordContext raised an exception."
    
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
