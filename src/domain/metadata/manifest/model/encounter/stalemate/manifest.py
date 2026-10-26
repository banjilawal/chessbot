# src/domain/metadata/manifest/model/encounter/stalemate/manifest.py

"""
Module: domain.metadata.manifest.model.encounter.stalemate.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    StalemateEncounter, StalemateNullWarningSet,
    StalemateEncounterTypeUnion, EncounterManifest
)

class StalemateEncounterManifest(EncounterManifest[StalemateEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the StalemateEncounter
            security lifecycle.

     Attributes:
        types: StalemateEncounterTypeUnion
        nulls: StalemateEncounterNullGroup

     Provides:

     Super Class:
        EncounterManifest
     """
    
    def __init__(
            self,
            types: Optional[StalemateEncounterTypeUnion] | None = None,
            nulls: Optional[StalemateNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[StalemateEncounterTypeUnion]
            nulls: Optional[StalemateEncounterNullGroup]
        """
        super().__init__(
            types=types or StalemateEncounterTypeUnion(),
            nulls=nulls or StalemateNullWarningSet(),
        )
    
    @property
    def types(self) -> StalemateEncounterTypeUnion:
        return cast(StalemateEncounterTypeUnion, super().types)
    
    @property
    def nulls(self) -> StalemateNullWarningSet:
        return cast(StalemateNullWarningSet, super().nulls)