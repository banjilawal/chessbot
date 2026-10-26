# src/domain/metadata/manifest/struct/binder/manifest.py

"""
Module: domain.metadata.manifest.struct.binder.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import ArchetypeBinder, BinderNullWarningSet, StructManifest, BinderLayer

T = TypeVar("T", bound="ArchetypeBinder")

class BinderManifest(StructManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Binder security lifecycle.

     Attributes:
        types: BinderTypeUnion[T]
        nulls: BinderNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: BinderLayer[T],
            nulls: BinderNullWarningSet[T],
    ):
        """
        Args:
            types: BinderTypeUnion[T]
            nulls: BinderNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> BinderLayer[T]:
        return cast(BinderLayer[T], super().types)
    
    @property
    def nulls(self) -> BinderNullWarningSet:
        return cast(BinderNullWarningSet, super().nulls)