# src/assurance/depend/wrapper/model/square/depend.py

"""
Module: assurance.depend.wrapper.model.square.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Square
from exchange import (
    BoardValidationServer, CoordValidationServer, TokenValidationServer
)


class SquareWrapperDependency(ModelWrapperDependency[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy SqaureValidator's ResponseWrapper dependencies.

    Attributes:
        board: BoardValidationServer
        coord: CoordValidationServer
        token: TokenValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _board: BoardValidationServer
    _coord: CoordValidationServer
    _token: TokenValidationServer
    
    def __init__(
            self,
            board: Optional[BoardValidationServer] | None = None,
            coord: Optional[CoordValidationServer] | None = None,
            token: Optional[TokenValidationServer] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
            coord: Optional[CoordValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationServer()
        self._coord = coord or CoordValidationServer()
        self._token = token or TokenValidationServer()
        
    @property
    def board(self) -> BoardValidationServer:
        return self._board
    
    @property
    def coord(self) -> CoordValidationServer:
        return self._coord
    
    @property
    def token(self) -> TokenValidationServer:
        return self._token