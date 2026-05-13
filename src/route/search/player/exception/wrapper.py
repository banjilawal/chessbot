# src/logic/player/route/exception/validator.py

"""
Module: logic.player.route.exception.work
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PLAYER_SEARCH_FAILURE #======================#
    "PlayerSearchException",
]

from system import SearchException


# ======================# PLAYER_SEARCH_FAILURE #======================#
class PlayerSearchException(SearchException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that a player search was not completed, it returned an error instead of a
        work product. 
    2.  Trace the method calls.

    Super Class:
        *   SearchException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See SearchException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See SearchException class for inherited methods.
    """
    OP = "Search"
    MTHD_RSLT = "SearchResult"
    ERR_CODE = "PLAYER_SEARCH_FAILURE"
    MSG = "Player search method failed."
 
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )

__all__ = [
    # ======================# PLAYER_SEARCH_FAILURE #======================#
    "PlayerSearchException",
]

from system import SearchException
from logic.player import PlayerException


# ======================# PLAYER_SEARCH_FAILURE #======================#
class PlayerSearchException(PlayerException, SearchException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a player search operation failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   FinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
