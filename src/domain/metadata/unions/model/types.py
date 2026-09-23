# src/domain/metadata/unions/strcture/manifest.py

"""
Module: domain.metadata.unions.model.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Model, ModelBlueprint, TypeUnion
from transit import EntityCarrier

T = TypeVar("T", bound="Model")


class ModelTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Model.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[ModelBlueprint[T]]
        
    Provides:

    Super Class:
        TypeUnion
    """
    _model: Type[T]
    _carrier: Type[EntityCarrier[T]]
    _blueprint: Type[ModelBlueprint[T]]
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[EntityCarrier[T]],
            blueprint: Type[ModelBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[ModelBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
        self._carrier = carrier
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[T]]:
        return self._carrier
    
    @property
    def blueprint(self) -> Type[ModelBlueprint[T]]:
        return cast(Type[ModelBlueprint[T]], super().model)