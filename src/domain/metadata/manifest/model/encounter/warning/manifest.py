# src/domain/metadata/manifest/model/encounter/warning/manifest.py

"""
Module: domain.metadata.manifest.model.encounter.warning.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    EncounterWarningNullGroup, EncounterWarning, EncounterWarningTypeUnion,
    EncounterManifest
)


class EncounterWarningManifest(EncounterManifest[EncounterWarning]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the EncounterWarning 
            security lifecycle.

     Attributes:
        types: EncounterWarningTypeUnion
        nulls: EncounterWarningNullGroup

     Provides:

     Super Class:
        EncounterManifest
     """
    
    def __init__(
            self,
            types: Optional[EncounterWarningTypeUnion] | None = None,
            nulls: Optional[EncounterWarningNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[EncounterWarningTypeUnion]
            nulls: Optional[EncounterWarningNullGroup]
        """
        super().__init__(
            types=types or EncounterWarningTypeUnion(),
            nulls=nulls or EncounterWarningNullGroup(),
        )
    
    @property
    def types(self) -> EncounterWarningTypeUnion:
        return cast(EncounterWarningTypeUnion, super().types)
    
    @property
    def nulls(self) -> EncounterWarningNullGroup:
        return cast(EncounterWarningNullGroup, super().nulls)