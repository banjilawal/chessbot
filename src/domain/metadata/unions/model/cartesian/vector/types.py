# src/domain/metadata/unions/cartesian/vector/types.py

"""
Module: domain.metadata.unions.cartesian.vector.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import CartesianTypeUnion, Vector, VectorBlueprint
from transit import VectorCarrier


class VectorTypeUnion(CartesianTypeUnion[Vector]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Vector.

    Attributes:
        model: Type[Vector]
        carrier: Type[VectorCarrier]
        blueprint: Type[VectorBlueprint]

    Provides:

    Super Class:
        CartesianTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Vector]] | None = None,
            carrier: Optional[Type[VectorCarrier]] | None = None, 
            blueprint: Optional[Type[VectorBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Vector]]
            carrier: Optional[Type[VectorCarrier]]
            blueprint: Optional[Type[VectorBlueprint]]
        """
        super().__init__(
            model=model or Vector, 
            carrier=carrier or VectorCarrier, 
            blueprint=blueprint or VectorBlueprint
        )
    
    @property
    def model(self) -> Type[Vector]:
        return cast(Type[Vector], super().model)
    
    @property
    def carrier(self) -> Type[VectorCarrier]:
        return cast(Type[VectorCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[VectorBlueprint]:
        return cast(Type[VectorBlueprint], super().blueprint)