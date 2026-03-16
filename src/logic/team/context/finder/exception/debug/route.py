# src/logic/team/context/finder/exception/debug/route.py

"""
Module: logic.team.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NO_TEAM_SEARCH_ROUTE_ROUTE_EXCEPTION #======================#
    "TeamSearchRouteException",
]

from logic.team import TeamDebugException


# ======================# NO_TEAM_SEARCH_ROUTE_ROUTE_EXCEPTION #======================#
class TeamSearchRouteException(TeamDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that there was no search logic for a team attribute.

    # PARENT:
        *   TeamDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   TeamDebugException class for inherited attributes.

    # CONSTRUCTOR:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See TeamDebugException class for inherited methods.
    """
    ERR_CODE = "NO_TEAM_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "There is no search logic for the team attribute."
    
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
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
