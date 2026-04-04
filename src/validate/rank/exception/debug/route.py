# src/logic/schema/database/search/context/service/operation/validation/exception/route.py

"""
Module: logic.schema.database.search.context.service.operation.validation.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# RANK_VALIDATION_ROUTE_EXCEPTION #======================#
    "RankValidationRouteException",
]

from system import ExecutionRouteException

# ======================# RANK_VALIDATION_ROUTE_EXCEPTION #======================#
class RankValidationRouteException(ExecutionRouteException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that a rank validation failed because there was no
            validation path for its subclass.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        ExecutionRouteException
    """
    ERR_CODE = "RANK_VALIDATION_ROUTE_EXCEPTION"
    MSG = "No validation path exists for the Rank's subclass."
    
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