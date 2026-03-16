# src/logic/player/context/finder/exception/debug/route.py

"""
Module: logic.player.context.finder.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NO_PLAYER_SEARCH_ROUTE_ROUTE_EXCEPTION #======================#
    "PlayerSearchRouteException",
]

from logic.player import PlayerDebugException


# ======================# NO_PLAYER_SEARCH_ROUTE_ROUTE_EXCEPTION #======================#
class PlayerSearchRouteException(PlayerDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that there was no search logic for a player attribute.

    # PARENT:
        *   PlayerDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   PlayerDebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See PlayerDebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "NO_PLAYER_SEARCH_ROUTE_ROUTE_EXCEPTION"
    MSG = "There is no search logic for the player attribute."
    
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
