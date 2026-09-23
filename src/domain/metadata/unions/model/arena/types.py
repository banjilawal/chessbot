# src/domain/metadata/unions/arena/types.py

"""
Module: domain.metadata.unions.arena.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Arena, ArenaBlueprint, TypeUnion
from transit import ArenaCarrier


class ArenaTypeUnion(TypeUnion[Arena]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Arena.

    Attributes:
        model: Type[Arena]
        carrier: Type[ArenaCarrier]
        blueprint: Type[ArenaBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Arena]] | None = None,
            carrier: Optional[Type[ArenaCarrier]] | None = None, 
            blueprint: Optional[Type[ArenaBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Arena]]
            carrier: Optional[Type[ArenaCarrier]
            blueprint: Optional[Type[ArenaBlueprint] 
        """
        super().__init__(
            model=model or Arena, 
            carrier=carrier or ArenaCarrier, 
            blueprint=blueprint or ArenaBlueprint
        )
    
    @property
    def model(self) -> Type[Arena]:
        return cast(Type[Arena], super().model)
    
    @property
    def carrier(self) -> Type[ArenaCarrier]:
        return cast(Type[ArenaCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[ArenaBlueprint]:
        return cast(Type[ArenaBlueprint], super().blueprint)