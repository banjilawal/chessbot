# src/blueprint/container/coord/blueprint.py

"""
Module: blueprint.container.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import ContainerBlueprint
from container import Coord


class CoordBlueprint(ContainerBlueprint[Coord]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Coord object.

    Attributes:
        row: int
        column: int
        
    Provides:

     Super Class:
        ContainerBlueprint
     """
    _row: int
    _column: int
    
    def __init__(
            self,
            row: int,
            column: int,
            container_class: Type[Coord] = Coord,
    ):
        """
        Args:
            row: int
            column: int
            container_class: Type[Coord]
        """
        super().__init__(container_class=container_class)
        self._row = row
        self._column = column
        
    @property
    def mode_class(self) -> Type[Coord]:
        return cast(Type[Coord], self.container_class)
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column