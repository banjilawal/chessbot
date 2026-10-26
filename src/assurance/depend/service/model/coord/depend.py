# src/assurance/depend/service/model/coord/depend.py

"""
Module: assurance.depend.service.model.coord.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Coord
from exchange import BoardValidationService


class CoordDependency(ModelDependency[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy CoordValidator's ResponseService dependencies.

    Attributes:
        board: BoardValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    
    _board: BoardValidationService
    
    def __init__(
            self,
            board: Optional[BoardValidationService] | None = None,
    ):
        """
        Args:
            board: Optional[BoardValidatorClient]
        """
        super().__init__()
        self._board = board or BoardValidationService()
    
    @property
    def board(self) -> BoardValidationService:
        return self._board
    
