# src/domain/metadata/unions/model/encounter/types.py

"""
Module: domain.metadata.unions.encounter.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, Type, TypeVar, cast

from domain import ModelTypeUnion, Encounter, EncounterBlueprint
from transit import EncounterCarrier

T = TypeVar("T", bound="Encounter")


class EncounterTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Encounter.

    Attributes:
        model: Type[Encounter]
        carrier: Type[EncounterCarrier]
        blueprint: Type[EncounterBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[T]] | None = None,
            carrier: Optional[Type[EncounterCarrier[T]]] | None = None,
            blueprint: Optional[Type[EncounterBlueprint[T]]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[T]]
            carrier: Optional[Type[EncounterCarrier[T]]]
            blueprint: Optional[Type[EncounterBlueprint[T]]]
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