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
    BoardValidationResponseWrapper, CoordValidationResponseWrapper
)


class SquareWrapperDependency(ModelWrapperDependency[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy SqaureValidator's ResponseWrapper dependencies.

    Attributes:
        board: BoardValidationResponseWrapper
        coord: CoordValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _board: BoardValidationResponseWrapper
    _coord: CoordValidationResponseWrapper
    
    def __init__(
            self,
            board: Optional[BoardValidationResponseWrapper] | None = None,
            coord: Optional[CoordValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
            coord: Optional[CoordValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationResponseWrapper()
        self._coord = coord or CoordValidationResponseWrapper()
        
    @property
    def board(self) -> BoardValidationResponseWrapper:
        return self._board
    
    @property
    def coord(self) -> CoordValidationResponseWrapper:
        return self._coord