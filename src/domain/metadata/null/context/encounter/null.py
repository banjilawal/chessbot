# src/domain/metadata/null/context/encounter/null.py

"""
Module: domain.metadata.null.context.encounter.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ContextNullWarningSet, Encounter
from err import (
    EncounterContextBlueprintNullException, EncounterContextCarrierNullException,
    EncounterContextNullException
)

T = TypeVar("T", bound="Encounter")

class EncounterContextNullWarningSet(ContextNullWarningSet[T], Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Encounter's integrity cycle.

    Attributes:
        model: EncounterContextNullException
        carrier: AttackContextCarrierNullException
        blueprint: AttackContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[EncounterContextNullException] | None = None,
            carrier: Optional[EncounterContextCarrierNullException] | None = None,
            blueprint: Optional[EncounterContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterContextNullException]
            carrier: Optional[AttackContextCarrierNullException]
            blueprint: Optional[AttackContextBlueprintNullException]
        """
        super().__init__(
            model=model or EncounterContextNullException(),
            carrier =carrier or EncounterContextCarrierNullException(),
            blueprint =blueprint or EncounterContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> EncounterContextNullException:
        return cast(EncounterContextNullException, super().model)
    
    @property
    def carrier(self) -> EncounterContextCarrierNullException:
        return cast(EncounterContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> EncounterContextBlueprintNullException:
        return cast(EncounterContextBlueprintNullException, super().blueprint)