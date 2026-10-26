# src/domain/metadata/manifest/model/encounter/kill/manifest.py

"""
Module: domain.metadata.manifest.model.encounter.kill.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    KillEncounterNullGroup, KillEncounter, EncounterManifest, KillLayer
)


class KillEncounterManifest(EncounterManifest[KillEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the KillEncounter
            security lifecycle.

     Attributes:
        types: KillEncounterTypeUnion
        nulls: KillEncounterNullGroup

     Provides:

     Super Class:
        EncounterManifest
     """
    
    def __init__(
            self,
            types: Optional[KillLayer] | None = None,
            nulls: Optional[KillEncounterNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[KillEncounterTypeUnion]
            nulls: Optional[KillEncounterNullGroup]
        """
        super().__init__(
            types=types or KillLayer(),
            nulls=nulls or KillEncounterNullGroup(),
        )
    
    @property
    def types(self) -> KillLayer:
        return cast(KillLayer, super().types)
    
    @property
    def nulls(self) -> KillEncounterNullGroup:
        return cast(KillEncounterNullGroup, super().nulls)