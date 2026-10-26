# src/domain/metadata/unions/context/arena/types.py

"""
Module: domain.metadata.unions.context.arena.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Arena, ArenaContextBlueprint, ContextLayer
from transit import ArenaContextCarrier


class ArenaContextLayer(ContextLayer[ArenaContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Arena.

    Attributes:
        model: Type[ArenaContext]
        carrier: Type[ArenaContextCarrier]
        blueprint: Type[ArenaContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[ArenaContext]] | None = None,
            carrier: Optional[Type[ArenaContextCarrier]] | None = None,
            blueprint: Optional[Type[ArenaContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[ArenaContext]]
            carrier: Optional[Type[ArenaContextCarrier]
            blueprint: Optional[Type[ArenaContextBlueprint] 
        """
        super().__init__(
            model=model or ArenaContext, 
            carrier=carrier or ArenaContextCarrier, 
            blueprint=blueprint or ArenaContextBlueprint
        )
    
    @property
    def model(self) -> Type[ArenaContext]:
        return cast(Type[ArenaContext], super().model)
    
    @property
    def carrier(self) -> Type[ArenaContextCarrier]:
        return cast(Type[ArenaContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[ArenaContextBlueprint]:
        return cast(Type[ArenaContextBlueprint], super().contextBlueprint)