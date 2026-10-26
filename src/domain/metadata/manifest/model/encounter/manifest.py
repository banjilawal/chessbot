# src/domain/metadata/manifest/model/encounter/encounter/manifest.py

"""
Module: domain.metadata.manifest.model.encounter.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelManifest, Encounter, EncounterNullGroup, EncounterLayer

T = TypeVar("T", bound="Encounter")

class EncounterManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Encounter
            security lifecycle.

     Attributes:
        types: EncounterTypeUnion[T]
        nulls: EncounterNullGroup[T]

     Provides:

     Super Class:
        ModelManifest
     """

    def __init__(
            self,
            types: Optional[EncounterLayer[T]] | None = None,
            nulls: Optional[EncounterNullGroup[T]] | None = None,
    ):
        """
        Args:
            types: EncounterTypeUnion[T]
            nulls: EncounterNullGroup[T]
        """
        super().__init__(
            types=types or EncounterLayer(),
            nulls=nulls or EncounterNullGroup(),
        )

    @property
    def types(self) -> EncounterLayer[T]:
        return cast(EncounterLayer[T], super().types)

    @property
    def nulls(self) -> EncounterNullGroup[T]:
        return cast(EncounterNullGroup[T], super().nulls)