# src/domain/metadata/nulls/model/encounter/group.py

"""
Module: domain.metadata.nulls.model.encounter.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelNullGroup, Encounter
from err import (
    EncounterBlueprintNullException, EncounterCarrierNullException,
    EncounterNullException
)

T = TypeVar("T", bound="Encounter")

class EncounterNullGroup(ModelNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Encounter's integrity cycle.

    Attributes:
        model: EncounterNullException
        carrier: AttackCarrierNullException
        blueprint: AttackBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[EncounterNullException] | None = None,
            carrier: Optional[EncounterCarrierNullException] | None = None,
            blueprint: Optional[EncounterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterNullException]
            carrier: Optional[AttackCarrierNullException]
            blueprint: Optional[AttackBlueprintNullException]
        """
        super().__init__(
            model = model or EncounterNullException(),
            carrier =carrier or EncounterCarrierNullException(),
            blueprint =blueprint or EncounterBlueprintNullException(),
        )
        
    @property
    def model(self) -> EncounterNullException:
        return cast(EncounterNullException, super().model)
    
    @property
    def carrier(self) -> EncounterCarrierNullException:
        return cast(EncounterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> EncounterBlueprintNullException:
        return cast(EncounterBlueprintNullException, super().blueprint)