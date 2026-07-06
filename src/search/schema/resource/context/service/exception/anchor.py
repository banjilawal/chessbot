# src/logic/schema/database/searcher/context/service/exception/anchor.py

"""
Module: logic.schema.database.searcher.context.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SCHEMA_CONTEXT_SERVICE_EXCEPTION #======================#
    "SchemaContextServiceException",
]

from system import ServiceException


# ======================# SCHEMA_CONTEXT_SERVICE_EXCEPTION #======================#
class SchemaContextServiceException(ServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors SchemaContextService debug (layer-2) information.
        2.  Indicate which SchemaContextService method received a  worker's (layer-1)
            failure result.

    Attributes:
        msg: Optional[str]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:

    Super Class:
        ServiceException
    """
    ERR_CODE = "SCHEMA_CONTEXT_SERVICE_EXCEPTION"
    MSG = "SchemaContextService raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
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
        super().__init__(
            ex=ex,
            msg=msg,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            err_code=err_code,
        )