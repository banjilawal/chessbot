# src/domain/metadata/unions/walk/types.py

"""
Module: domain.metadata.unions.walk.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Walk, WalkBlueprint, TypeUnion
from transit import WalkCarrier


class WalkTypeUnion(TypeUnion[Walk]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Walk.

    Attributes:
        model: Type[Walk]
        carrier: Type[WalkCarrier]
        blueprint: Type[WalkBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Walk]] | None = None,
            carrier: Optional[Type[WalkCarrier]] | None = None, 
            blueprint: Optional[Type[WalkBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Walk]]
            carrier: Optional[Type[WalkCarrier]
            blueprint: Optional[Type[WalkBlueprint] 
        """
        super().__init__(
            model=model or Walk, 
            carrier=carrier or WalkCarrier, 
            blueprint=blueprint or WalkBlueprint
        )
    
    @property
    def model(self) -> Type[Walk]:
        return cast(Type[Walk], super().model)
    
    @property
    def carrier(self) -> Type[WalkCarrier]:
        return cast(Type[WalkCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[WalkBlueprint]:
        return cast(Type[WalkBlueprint], super().blueprint)