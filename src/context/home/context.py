# src/context/home/model/state.py

"""
Module: context.home.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from context import Context
from model import Board, HomeSquare, Token


class TokenHomeContext(Context[HomeSquare]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply an attribute-value search filter.

    Attributes:
        token: Optional[Token]
        board: Optional[Board]
        square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    token: Optional[Token] | None = None
    board: Optional[Board] | None = None
    square_name: Optional[str] | None = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "token": self.arena,
            "board": self.player,
            "square_name": self.square_name
        }
