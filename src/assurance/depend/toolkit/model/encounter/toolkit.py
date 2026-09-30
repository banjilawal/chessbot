# src/assurance/depend/toolkit/model/encounter/toolkit.py

"""
Module: assurance.depend.toolkit.model.encounter.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, EncounterWrapperDependency
from domain import Encounter, EncounterTypeUnion


class EncounterValidatorToolkit(ModelValidatorToolkit[Encounter]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Encounter attribute validators and type metadata.

    Attributes:
        helper: EncounterManifest
        metadata: EncounterHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[EncounterManifest] | None = None,
            wrapper: Optional[EncounterWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[EncounterManifest]
            metadata: Optional[EncounterHelperTable]
        """
        super().__init__(
            wrapper=wrapper or EncounterWrapperDependency(),
            metadata=metadata or EncounterManifest(),
        )
    
    @property
    def wrapper(self) -> EncounterWrapperDependency:
        return cast(EncounterWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> EncounterManifest:
        return cast(EncounterManifest, super().metadata)
    
    @property
    def nulls(self) -> EncounterNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> EncounterTypeUnion:
        return self.metadata.types