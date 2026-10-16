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
from exchange import BoardValidationServer


class CoordWrapperDependency(ModelWrapperDependency[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy CoordValidator's ResponseWrapper dependencies.

    Attributes:
        board: BoardValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _board: BoardValidationServer
    
    def __init__(
            self,
            board: Optional[BoardValidationServer] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationServer()
    
    @property
    def board(self) -> BoardValidationServer:
        return self._board
    
