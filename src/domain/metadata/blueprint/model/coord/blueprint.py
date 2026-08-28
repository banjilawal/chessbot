# src/domain/metadata/blueprint/model/coord/blueprint.py

"""
Module: domain.metadata.blueprint.model.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Type, cast

from domain.metadata.blueprint import ModelBlueprint
from domain.model import Coord


class CoordBlueprint(ModelBlueprint[Coord]):
    """
    Role:
        - Container

    Responsibilities:
        1.  Provides values for hydrating a Coord object.

    Attributes:
        row: int
        column: int
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _row: int
    _column: int
    
    def __init__(
            self,
            row: int,
            column: int,
            domain_class: Type[Coord] = Coord,
    ):
        """
        Args:
            row: int
            column: int
            domain_class: Type[Coord]
        """
        super().__init__(domain_class=domain_class)
        self._row = row
        self._column = column
        
    @property
    def domain_class(self) -> Type[Coord]:
        return cast(Type[Coord], super().domain_class)
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column