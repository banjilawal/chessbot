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
    BoardValidationService, CoordValidationService, TokenValidationService
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
    _board: BoardValidationService
    _coord: CoordValidationService
    _token: TokenValidationService
    
    def __init__(
            self,
            board: Optional[BoardValidationService] | None = None,
            coord: Optional[CoordValidationService] | None = None,
            token: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
            coord: Optional[CoordValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationService()
        self._coord = coord or CoordValidationService()
        self._token = token or TokenValidationService()
        
    @property
    def board(self) -> BoardValidationService:
        return self._board
    
    @property
    def coord(self) -> CoordValidationService:
        return self._coord
    
    @property
    def token(self) -> TokenValidationService:
        return self._token