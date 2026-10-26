# src/domain/metadata/context/manifest/context/encounter/encounter/manifest.py

"""
Module: domain.metadata.manifest.context.encounter.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


class EncounterContextManifest(ContextManifest[Encounter]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the Encounter
            security lifecycle.

     Attributes:
        types: EncounterContextTypeUnion[T]
        nulls: EncounterContextNullGroup[T]

     Provides:

     Super Class:
        ContextManifest
     """

    def __init__(
            self,
            types: Optional[EncounterContextTypeUnion[T]] | None = None,
            nulls: Optional[EncounterContextNullGroup[T]] | None = None,
    ):
        """
        Args:
            types: EncounterContextTypeUnion[T]
            nulls: EncounterContextNullGroup[T]
        """
        super().__init__(
            types=types or EncounterContextTypeUnion(),
            nulls=nulls or EncounterContextNullGroup(),
        )

    @property
    def types(self) -> EncounterContextTypeUnion[T]:
        return cast(EncounterContextTypeUnion[T], super().types)

    @property
    def nulls(self) -> EncounterContextNullGroup[T]:
        return cast(EncounterContextNullGroup[T], super().nulls)