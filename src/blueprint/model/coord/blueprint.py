# src/blueprint/model/column/blueprint.py

"""
Module: blueprint.model.column.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import ModelBlueprint
from model import Coord


class ColumnBlueprint(ModelBlueprint[Coord]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Column object.

    Attributes:
       row:Row,
        column: Column
        id: Optional[int]
        formation Optional[Formation]
        model_class: Type[Column]
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _row: int
    _column: int
    
    def __init__( self, row: int,  column: int, model_class: Type[Coord],):
        """
        Args:
            row: int
            column: int
            model_class: Type[Coord]
        """
        super().__init__(model_class=model_class)
        self._row = int
        self._column = int
        
    @property
    def mode_class(self) -> Type[Coord]:
        return cast(Type[Coord], self.model_class)
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column