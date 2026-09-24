# src/domain/metadata/unions/model/path/types.py

"""
Module: domain.metadata.unions.path.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Path, PathBlueprint, ModelTypeUnion
from transit import PathCarrier



class PathTypeUnion(ModelTypeUnion[Path]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Path.

    Attributes:
        model: Type[Path]
        carrier: Type[PathCarrier]
        blueprint: Type[PathBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Path]] | None = None,
            carrier: Optional[Type[PathCarrier]] | None = None, 
            blueprint: Optional[Type[PathBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Path]]
            carrier: Optional[Type[PathCarrier]
            blueprint: Optional[Type[PathBlueprint] 
        """
        super().__init__(
            model=model or Path, 
            carrier=carrier or PathCarrier, 
            blueprint=blueprint or PathBlueprint
        )
    
    @property
    def model(self) -> Type[Path]:
        return cast(Type[Path], super().model)
    
    @property
    def carrier(self) -> Type[PathCarrier]:
        return cast(Type[PathCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[PathBlueprint]:
        return cast(Type[PathBlueprint], super().blueprint)