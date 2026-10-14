# src/domain/metadata/unions/strcture/binder/manifest.py

"""
Module: domain.metadata.unions.struct.binder.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import ArchetypeBinder, Archetyped, BinderBlueprint, StructTypeUnion
from transit import BinderCarrier, StructCarrier

T = TypeVar("T", bound="ArchetypeBinder")
M = TypeVar("M", bound="Archetyped")

class BinderTypeUnion(StructTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Binder.

    Attributes:
        model: Type[T]
        carrier: Type[BinderCarrier[T]]
        blueprint: Type[BinderBlueprint[T]]
        
    Provides:

    Super Class:
        StructTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[BinderCarrier[T]],
            blueprint: Type[BinderBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[BinderCarrier[T]]
            blueprint: Type[BinderBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint, carrier=carrier)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[BinderCarrier[T]]:
        return cast(Type[BinderCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[BinderBlueprint[T]]:
        return cast(Type[BinderBlueprint[T]], super().model)