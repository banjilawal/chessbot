# src/logic/player/_/build/exception/route.py

"""
Module: logic.player..build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PLAYER_BUILD_ROUTE_EXCEPTION #======================#
    "PlayerBuildRouteException",
]

from logic.system import ExecutionRouteException


# ======================# PLAYER_BUILD_ROUTE_EXCEPTION #======================#
class PlayerBuildRouteException(ExecutionRouteException):
    """
    Role:Error Tracing, Debugging, Super Exception

    Responsibilities:
    1.  Indicate that the PlayerFactory does not have abuild rout for a Player subclass..

    Super Class:
        *   ExecutionRoute

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ExecutionRoute class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ExecutionRoute class for inherited methods.
    """
    ERR_CODE = "PLAYER_BUILD_ROUTE_EXCEPTION"
    MSG = "No Build route for Player subclass."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)