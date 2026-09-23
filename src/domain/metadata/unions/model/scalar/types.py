# src/domain/metadata/unions/scalar/types.py

"""
Module: domain.metadata.unions.scalar.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Scalar, ScalarBlueprint, TypeUnion
from transit import ScalarCarrier


class ScalarTypeUnion(TypeUnion[Scalar]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Scalar.

    Attributes:
        model: Type[Scalar]
        carrier: Type[ScalarCarrier]
        blueprint: Type[ScalarBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Scalar]] | None = None,
            carrier: Optional[Type[ScalarCarrier]] | None = None, 
            blueprint: Optional[Type[ScalarBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Scalar]]
            carrier: Optional[Type[ScalarCarrier]
            blueprint: Optional[Type[ScalarBlueprint] 
        """
        super().__init__(
            model=model or Scalar, 
            carrier=carrier or ScalarCarrier, 
            blueprint=blueprint or ScalarBlueprint
        )
    
    @property
    def model(self) -> Type[Scalar]:
        return cast(Type[Scalar], super().model)
    
    @property
    def carrier(self) -> Type[ScalarCarrier]:
        return cast(Type[ScalarCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[ScalarBlueprint]:
        return cast(Type[ScalarBlueprint], super().blueprint)