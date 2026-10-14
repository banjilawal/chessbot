# src/domain/metadata/unions/strcture/types.py

"""
Module: domain.metadata.unions.struct.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Struct, StructBlueprint, TypeUnion
from transit import StructCarrier

T = TypeVar("T", bound="Struct")
M = TypeVar("M")


class StructTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Struct.

    Attributes:
        model: Type[T]
        blueprint: Type[StructBlueprint[T]]
        
    Provides:

    Super Class:
        TypeUnion
    """
    _model: Type[T]
    _carrier: Type[StructCarrier[T]]
    _blueprint: Type[StructBlueprint[T, M]]
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[StructCarrier[T]],
            blueprint: Type[StructBlueprint[T, M]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[StructCarrier[T]]
            blueprint: Type[StructBlueprint[T, M]]
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[StructCarrier[T]]:
        return cast(Type[StructCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[StructBlueprint[T, M]]:
        return cast(Type[StructBlueprint[T, M]], super().blueprint)