# src/domain/metadata/unions/context/vector/types.py

"""
Module: domain.metadata.unions.context.vector.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ContextTypeUnion, VectorContextBlueprint
from transit import VectorContextCarrier


class VectorContextTypeUnion(ContextTypeUnion[VectorContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Vector.

    Attributes:
        model: Type[VectorContext]
        carrier: Type[VectorContextCarrier]
        blueprint: Type[VectorContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[VectorContext]] | None = None,
            carrier: Optional[Type[VectorContextCarrier]] | None = None,
            blueprint: Optional[Type[VectorContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[VectorContext]]
            carrier: Optional[Type[VectorContextCarrier]]
            blueprint: Optional[Type[VectorContextBlueprint]]
        """
        super().__init__(
            model=model or VectorContext, 
            carrier=carrier or VectorContextCarrier, 
            blueprint=blueprint or VectorContextBlueprint
        )
    
    @property
    def model(self) -> Type[VectorContext]:
        return cast(Type[VectorContext], super().model)
    
    @property
    def carrier(self) -> Type[VectorContextCarrier]:
        return cast(Type[VectorContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[VectorContextBlueprint]:
        return cast(Type[VectorContextBlueprint], super().contextBlueprint)