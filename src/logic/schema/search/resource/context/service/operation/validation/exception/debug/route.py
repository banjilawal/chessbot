# src/logic/schema/database/search/context/service/operation/validation/exception/debug/route.py

"""
Module: logic.schema.database.search.context.service.operation.validation.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SCHEMA_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
    "SchemaContextValidationRouteException",
]

from logic.system import ContextRouteException


# ======================# SCHEMA_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
class SchemaContextValidationRouteException(ContextRouteException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that no SchemaContext validation failed because attribute
            did not have a verification path.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        ContextRouteException
    """
    MSG = str = "No validation path for the SchemaContext attribute."
    ERR_CODE = "SCHEMA_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
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
        )