# src/domain/metadata/unions/cartesian/coord/types.py

"""
Module: domain.metadata.unions.cartesian.coord.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CartesianTypeUnion, Coord, CoordBlueprint
from transit import CoordCarrier



class CoordTypeUnion(CartesianTypeUnion[Coord]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Coord.

    Attributes:
        model: Type[Coord]
        carrier: Type[CoordCarrier]
        blueprint: Type[CoordBlueprint]

    Provides:

    Super Class:
        CartesianTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Coord]] | None = None,
            carrier: Optional[Type[CoordCarrier]] | None = None, 
            blueprint: Optional[Type[CoordBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Coord]]
            carrier: Optional[Type[CoordCarrier]
            blueprint: Optional[Type[CoordBlueprint] 
        """
        super().__init__(
            model=model or Coord, 
            carrier=carrier or CoordCarrier, 
            blueprint=blueprint or CoordBlueprint
        )
    
    @property
    def model(self) -> Type[Coord]:
        return cast(Type[Coord], super().model)
    
    @property
    def carrier(self) -> Type[CoordCarrier]:
        return cast(Type[CoordCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CoordBlueprint]:
        return cast(Type[CoordBlueprint], super().blueprint)