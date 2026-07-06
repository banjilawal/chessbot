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


class TokenHomeContext:
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
    _token: Optional[Token]
    _board: Optional[Board]
    _square_name: Optional[str]
    
    def __init__(
            self,
            token: Optional[Token] | None = None,
            board: Optional[Board] | None = None,
            square_name: Optional[str] | None = None,
    ):
        """
        Args:
            token: Optional[Token]
            board: Optional[Board]
            square_name: Optional[str]
        """
        self._token = token
        self._board = board
        self._square_name = square_name
        
    @property
    def token(self) -> Optional[Token]:
        return self._token
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def square_name(self) -> Optional[str]:
        return self.square_name
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "token": self._token,
            "board": self._board,
            "square_name": self._square_name
        }
