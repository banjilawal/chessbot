# src/domain/metadata/unions/strcture/types.py

"""
Module: domain.metadata.unions.structure.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Structure, StructureBlueprint, TypeUnion

T = TypeVar("T", bound="Structure")


class StructureTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Structure.

    Attributes:
        model: Type[T]
        blueprint: Type[StructureBlueprint[T]]
        
    Provides:

    Super Class:
        TypeUnion
    """
    _model: Type[T]
    _blueprint: Type[StructureBlueprint[T]]
    
    def __init__(
            self,
            model: Type[T],
            blueprint: Type[StructureBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            blueprint: Type[StructureBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def blueprint(self) -> Type[StructureBlueprint[T]]:
        return cast(Type[StructureBlueprint[T]], super().model)