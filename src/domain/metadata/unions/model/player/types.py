# src/domain/metadata/unions/player/types.py

"""
Module: domain.metadata.unions.player.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, PlayerPoint, TypeUnion
from transit import EntityCarrier



T = TypeVar("T", bound="PlayerPoint")

class PlayerTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a PlayerPoint.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Type[T],
            carrier: Type[EntityCarrier[T]], 
            blueprint: Type[Blueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[Blueprint[T]] 
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)