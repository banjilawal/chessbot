# src/domain/metadata/manifest/model/attack/attack/manifest.py

"""
Module: domain.metadata.manifest.model.attack.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from domain import ModelManifest, Encounter, AttackNullGroup, AttackTypeUnion

T = TypeVar("T", bound="Encounter")

class AttackManifest(ModelManifest[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the Attack
            security lifecycle.

     Attributes:
        types: AttackTypeUnion
        nulls: AttackNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: AttackTypeUnion[T],
            nulls: AttackNullGroup[T]
    ):
        """
        Args:
            types: AttackTypeUnion[T]
            nulls: AttackNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls)
        
    @property
    def types(self) -> AttackTypeUnion[T]:
        return cast(AttackTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> AttackNullGroup[T]:
        return cast(AttackNullGroup[T], super().nulls)