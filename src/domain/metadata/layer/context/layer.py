# src/domain/metadata/unions/context/struct/types.py

"""
Module: domain.metadata.unions.context.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import ContextBlueprint, Layer
from transit import ContextCarrier

T = TypeVar("T", bound="Context")


class ContextLayer(Layer[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Model.

    Attributes:
        model: Type[T]
        carrier: Type[ContextCarrier[T]]
        blueprint: Type[ContextBlueprint[T]]
        
    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[ContextCarrier[T]],
            blueprint: Type[ContextBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[ContextCarrier[T]]
            blueprint: Type[ContextBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint, carrier=carrier)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[ContextCarrier[T]]:
        return cast(Type[ContextCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[ContextBlueprint[T]]:
        return cast(Type[ContextBlueprint[T]], super().model)