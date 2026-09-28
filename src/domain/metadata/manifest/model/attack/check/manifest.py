# src/domain/metadata/manifest/model/attack/check/manifest.py

"""
Module: domain.metadata.manifest.model.attack.check.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CheckWarningNullGroup, EncounterWarning, CheckWarningTypeUnion, AttackManifest
)


class CheckWarningManifest(AttackManifest[EncounterWarning]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the CheckWarning 
            security lifecycle.

     Attributes:
        types: CheckWarningTypeUnion
        nulls: CheckWarningNullGroup

     Provides:

     Super Class:
        AttackManifest
     """
    
    def __init__(
            self,
            types: Optional[CheckWarningTypeUnion] | None = None,
            nulls: Optional[CheckWarningNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CheckWarningTypeUnion]
            nulls: Optional[CheckWarningNullGroup]
        """
        super().__init__(
            types=types or CheckWarningTypeUnion(),
            nulls=nulls or CheckWarningNullGroup(),
        )
    
    @property
    def types(self) -> CheckWarningTypeUnion:
        return cast(CheckWarningTypeUnion, super().types)
    
    @property
    def nulls(self) -> CheckWarningNullGroup:
        return cast(CheckWarningNullGroup, super().nulls)