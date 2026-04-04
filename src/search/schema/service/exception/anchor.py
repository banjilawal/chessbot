# src/logic/schema/database/search/service/exception/anchor.py

"""
Module: logic.schema.database.search.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SCHEMA_SEARCH_SERVICE_FAILURE #======================#
    "SchemaSearchServiceException",
]

from system import ServiceException

# ======================# SCHEMA_SEARCH_SERVICE_FAILURE #======================#
class SchemaSearchServiceException(ServiceException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target

    Responsibilities:
        1.  Anchors SchemaLookupService debug (layer-2) information.
        2.  Indicate which SchemaLookupService method received a worker's
            (layer-1) failure result.


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
    CLS_NAME = "SchemaLookupService"
    ERR_CODE = "SCHEMA_SEARCH_SERVICE_FAILURE"
    MSG = "SchemaLookupService raised an exception."
    
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
