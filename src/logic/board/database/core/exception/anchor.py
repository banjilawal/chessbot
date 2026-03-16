# src/logic/board/database/core/exception/anchor.py

"""
Module: logic.board.database.core.exception.anchor
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# BOARD_STACK_SERVICE_EXCEPTION #======================#
    "BoardStackServiceException",
]

from logic.system import StackServiceException


# ======================# BOARD_STACK_SERVICE_EXCEPTION #======================#
class BoardStackServiceException(StackServiceException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Anchoring target for BoardStackService debug (layer-2) error state firing incident
        reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which BoardStackService method received a worker's (layer-1) failure result.

    # PARENT:
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackServiceException class for inherited attributes.

    # CONSTRUCTOR:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See StackServiceException class for inherited methods.
    """
    CLS_NAME = " BoardStackService"
    ERR_CODE = " BOARD_STACK_SERVICE_EXCEPTION"
    MSG = " BoardStackService raised an exception."
    
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
