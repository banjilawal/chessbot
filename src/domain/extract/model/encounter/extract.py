# src/domain/extract/model/encounter/extract.py

"""
Module: domain.extract.model.encounter.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelPrimeExtract, Encounter, EncounterBlueprint
from transit import EncounterCarrier

T = TypeVar("T", bound="Encounter")

class EncounterPrimeExtract(ModelPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for EncounterValidator.

    Attributes:
        carrier: EncounterCarrier
        blueprint: Optional[EncounterBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: EncounterCarrier[T],
            blueprint: Optional[EncounterBlueprint] | None = None,
    ):
        """
        Args:
            reference: EncounterCarrier[T]
            blueprint: Optional[EncounterBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> EncounterCarrier[T]:
        return cast(EncounterCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[EncounterBlueprint[T]]:
        return cast(EncounterBlueprint[T], super().blueprint)