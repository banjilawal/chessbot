# src/logic/edge/context/service/exception/anchor.py

"""
Module: logic.edge.context.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# EDGE_CONTEXT_SERVICE_EXCEPTION #======================#
    "EdgeContextServiceException",
]

from logic.system import ServiceException


# ======================# EDGE_CONTEXT_SERVICE_EXCEPTION #======================#
class EdgeContextServiceException(ServiceException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Anchoring target for EdgeContextService debug (layer-2) error state firing incident
        reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which EdgeContextService method received a worker's (layer-1) failure result.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ServiceException class for inherited attributes.

    # CONSTRUCTOR:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ServiceException class for inherited methods.
    """
    CLS_NAME = " EdgeContextService"
    ERR_CODE = " EDGE_CONTEXT_SERVICE_EXCEPTION"
    MSG = " EdgeContextService raised an exception."
    
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
