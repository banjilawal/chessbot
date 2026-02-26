# src/chess/game/exception.py

"""
Module: chess.game.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# GAME EXCEPTION #======================#
    "GameException",
]

from chess.system import SuperClassException


# ======================# GAME EXCEPTION #======================#
class GameException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of GameDebugException

    # PARENT:
    *   SuperClassException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_ERROR"
    MSG = "Game raised an exception."
    CLS_NAME = "Game"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.CLS_NAME
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name = cls_name)
