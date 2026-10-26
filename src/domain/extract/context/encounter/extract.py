# src/domain/extract/context/encounter/extract.py

"""
Module: domain.extract.context.encounter.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ContextPrimeExtract, Encounter, EncounterContextBlueprint
from transit import EncounterContextCarrier

T = TypeVar("T", bound="Encounter")

class EncounterContextPrimeExtract(ContextPrimeExtract[T], Generic[TContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for EncounterValidator.

    Attributes:
        contextCarrier: EncounterContextCarrier
        blueprint: Optional[EncounterContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: EncounterContextCarrier[T],
            blueprint: Optional[EncounterContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: EncounterContextCarrier[T]
            blueprint: Optional[EncounterContextBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> EncounterContextCarrier[T]:
        return cast(EncounterContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[EncounterContextBlueprint[T]]:
        return cast(EncounterContextBlueprint[T], super().blueprint)