# src/domain/metadata/unions/context/coord/types.py

"""
Module: domain.metadata.unions.context.coord.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Coord, CoordContextBlueprint, ContextTypeUnion
from transit import CoordContextCarrier



class CoordContextTypeUnion(ContextTypeUnion[CoordContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Coord.

    Attributes:
        model: Type[CoordContext]
        carrier: Type[CoordContextCarrier]
        blueprint: Type[CoordContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CoordContext]] | None = None,
            carrier: Optional[Type[CoordContextCarrier]] | None = None,
            blueprint: Optional[Type[CoordContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CoordContext]]
            carrier: Optional[Type[CoordContextCarrier]
            blueprint: Optional[Type[CoordContextBlueprint] 
        """
        super().__init__(
            model=model or CoordContext, 
            carrier=carrier or CoordContextCarrier, 
            blueprint=blueprint or CoordContextBlueprint
        )
    
    @property
    def model(self) -> Type[CoordContext]:
        return cast(Type[CoordContext], super().model)
    
    @property
    def carrier(self) -> Type[CoordContextCarrier]:
        return cast(Type[CoordContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[CoordContextBlueprint]:
        return cast(Type[CoordContextBlueprint], super().contextBlueprint)