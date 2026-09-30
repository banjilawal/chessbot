# src/domain/metadata/unions/model/encounter/types.py

"""
Module: domain.metadata.unions.encounter.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Encounter, EncounterBlueprint, ModelTypeUnion
from transit import EncounterCarrier

T = TypeVar("T", bound="Encounter")

class EncounterTypeUnion(ModelTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Encounter.

    Attributes:
        model: Type[T]
        carrier: Type[EncounterCarrier[T]
        blueprint: Type[EncounterBlueprint[T]
        
    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[EncounterCarrier[T]],
            blueprint: Type[EncounterBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]]
            carrier: Type[EncounterCarrier[T]]
            blueprint: Type[EncounterBlueprint[T]]
        """
        super().__init__(
            model=model or Encounter,
            carrier=carrier or EncounterCarrier,
            blueprint=blueprint or EncounterBlueprint,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[EncounterCarrier[T]]:
        return cast(Type[EncounterCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[EncounterBlueprint[T]]:
        return cast(Type[EncounterBlueprint[T]], super().blueprint)