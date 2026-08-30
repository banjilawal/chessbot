# src/domain/metadata/blueprint/model/searchable/cartesian/coord/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.cartesian.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import CartesianBlueprint, Coord, CoordContext
from err import CoordNullException


class CoordBlueprint(CartesianBlueprint[Coord]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Coord object.

    Attributes:
        row: int
        column: int
        domain_class: Type[Coord]
        domain_null_exception: CoordNullException
        search_context_class: Type[CoordContext]
        
    Provides:

     Super Class:
        CartesianBlueprint
     """
    _row: int
    _column: int
    
    def __init__(
            self,
            row: int,
            column: int,
            domain_class: Optional[Type[Coord]] | None = None,
            domain_null_exception: Optional[CoordNullException]| None = None,
            search_context_class: Optional[Type[CoordContext]] | None = None,
    ):
        """
        Args:
            row: int
            column: int
            domain_class: Optional[Type[Coord]]
            domain_null_exception: Optional[CoordNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Coord],
            domain_null_exception=domain_null_exception or CoordNullException(),
            search_context_class=search_context_class or Type[CoordContext],
        )
        self._row = row
        self._column = column
        
    @property
    def domain_class(self) -> Type[Coord]:
        return cast(Type[Coord], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[CoordContext]:
        return cast(Type[CoordContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> CoordNullException:
        return cast(CoordNullException, super().domain_null_exception)
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column