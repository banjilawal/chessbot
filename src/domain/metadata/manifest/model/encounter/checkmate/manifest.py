# src/domain/metadata/manifest/model/encounter/checkmate/manifest.py

"""
Module: domain.metadata.manifest.model.encounter.checkmate.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CheckmateEncounter, CheckmateNullWarningSet,
    CheckmateLayer, EncounterManifest
)

class CheckmateEncounterManifest(EncounterManifest[CheckmateEncounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the CheckmateEncounter
            security lifecycle.

     Attributes:
        types: CheckmateEncounterTypeUnion
        nulls: CheckmateEncounterNullGroup

     Provides:

     Super Class:
        EncounterManifest
     """
    
    def __init__(
            self,
            types: Optional[CheckmateLayer] | None = None,
            nulls: Optional[CheckmateNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[CheckmateEncounterTypeUnion]
            nulls: Optional[CheckmateEncounterNullGroup]
        """
        super().__init__(
            types=types or CheckmateLayer(),
            nulls=nulls or CheckmateNullWarningSet(),
        )
    
    @property
    def types(self) -> CheckmateLayer:
        return cast(CheckmateLayer, super().types)
    
    @property
    def nulls(self) -> CheckmateNullWarningSet:
        return cast(CheckmateNullWarningSet, super().nulls)