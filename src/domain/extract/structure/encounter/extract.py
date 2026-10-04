# src/domain/extract/struct/encounter/extract.py

"""
Module: domain.extract.struct.encounter.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import Blueprint, StructPrimeExtract, Encounter, EncounterBlueprint
from transit import EncounterCarrier

T = TypeVar("T", bound="Encounter")

class EncounterPrimeExtract(StructPrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for EncounterValidator.

    Attributes:
        carrier: EncounterCarrier
        blueprint: Optional[EncounterBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: EncounterCarrier[T],
            blueprint: Optional[EncounterBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: EncounterCarrier[T]
            blueprint: Optional[EncounterBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> EncounterCarrier[T]:
        return cast(EncounterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[EncounterBlueprint[T]]:
        return cast(EncounterBlueprint, super().blueprint)