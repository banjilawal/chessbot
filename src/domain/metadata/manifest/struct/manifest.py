# src/domain/metadata/manifest/struct/manifest.py

"""
Module: domain.metadata.manifest.struct.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import DomainManifest, Struct, StructNullGroup, StructLayer

T = TypeVar("T", bound="Struct")

class StructManifest(DomainManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Struct security lifecycle.

     Attributes:
        types: StructTypeUnion[T]
        nulls: StructNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: StructLayer[T],
            nulls: StructNullGroup[T],
    ):
        """
        Args:
            types: StructTypeUnion[T]
            nulls: StructNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> StructLayer[T]:
        return cast(StructLayer[T], super().types)
    
    @property
    def nulls(self) -> StructNullGroup:
        return cast(StructNullGroup, super().nulls)