# src/domain/metadata/unions/context/path/types.py

"""
Module: domain.metadata.unions.context.path.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Path, PathContextBlueprint, ContextTypeUnion
from transit import PathContextCarrier


class PathContextTypeUnion(ContextTypeUnion[PathContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Path.

    Attributes:
        model: Type[PathContext]
        carrier: Type[PathContextCarrier]
        blueprint: Type[PathContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[PathContext]] | None = None,
            carrier: Optional[Type[PathContextCarrier]] | None = None,
            blueprint: Optional[Type[PathContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[PathContext]]
            carrier: Optional[Type[PathContextCarrier]
            blueprint: Optional[Type[PathContextBlueprint] 
        """
        super().__init__(
            model=model or PathContext, 
            carrier=carrier or PathContextCarrier,
            blueprint=blueprint or PathContextBlueprint
        )
    
    @property
    def model(self) -> Type[PathContext]:
        return cast(Type[PathContext], super().model)
    
    @property
    def carrier(self) -> Type[PathContextCarrier]:
        return cast(Type[PathContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[PathContextBlueprint]:
        return cast(Type[PathContextBlueprint], super().contextBlueprint)