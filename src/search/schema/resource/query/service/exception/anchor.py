# src/logic/schema/database/search/context/service/exception/anchor.py

"""
Module: logic.schema.database.search.context.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SCHEMA_QUERY_SERVICE_EXCEPTION #======================#
    "SchemaQueryServiceException",
]

from system import ServiceException


# ======================# SCHEMA_QUERY_SERVICE_EXCEPTION #======================#
class SchemaQueryServiceException(ServiceException):
    """
    Role:Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Anchors SchemaQueryService debug (layer-2) error state firing incident
        reports on
            *   the triggering variable
            *   The trigger's value.
    2.  Indicate which SchemaQueryService method received a worker's (layer-1) failure result.

    Super Class:
        *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ServiceException class for inherited attributes.

    Attributes:
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
    CLS_NAME = "SchemaQueryService"
    ERR_CODE = "SCHEMA_QUERY_SERVICE_EXCEPTION"
    MSG = "SchemaQueryService raised an exception."
    
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)
