# src/domain/metadata/context/manifest/context/manifest.py

"""
Module: domain.metadata.manifest.context.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Context, ContextNullWarningSet, ContextLayer, DomainManifest

T = TypeVar("T", bound="Context")

class ContextManifest(DomainManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Context security lifecycle.

     Attributes:
        types: ContextTypeUnion[T]
        nulls: ContextNullGroup[T]

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: ContextLayer[T],
            nulls: ContextNullWarningSet[T],
    ):
        """
        Args:
            types: ContextTypeUnion[T]
            nulls: ContextNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> ContextLayer[T]:
        return cast(ContextLayer[T], super().types)
    
    @property
    def nulls(self) -> ContextNullWarningSet:
        return cast(ContextNullWarningSet, super().nulls)