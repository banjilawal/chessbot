# src/assurance/depend/wrapper/model/coord/depend.py

"""
Module: assurance.depend.wrapper.model.coord.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Coord
from exchange import BoardValidationResponseWrapper


class CoordWrapperDependency(ModelWrapperDependency[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy CoordValidator's ResponseWrapper dependencies.

    Attributes:
        board: BoardValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """

    _board: BoardValidationResponseWrapper
    
    def __init__(
            self,
            board: Optional[BoardValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationResponseWrapper()
    
    @property
    def board(self) -> BoardValidationResponseWrapper:
        return self._board
    
