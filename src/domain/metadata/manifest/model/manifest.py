# src/domain/metadata/manifest/model/manifest.py

"""
Module: domain.metadata.manifest.model.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Model, ModelNullGroup, ModelTypeUnion, ObjectManifest

T = TypeVar("T", bound="Model")

class ModelManifest(ObjectManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a Model's security lifecycle.

     Attributes:
        types: ModelTypeUnion[T]
        nulls: ModelNullGroup[T]

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: ModelTypeUnion[T],
            nulls: ModelNullGroup[T],
    ):
        """
        Args:
            types: ModelTypeUnion[T]
            nulls: ModelNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> ModelTypeUnion[T]:
        return cast(ModelTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> ModelNullGroup:
        return cast(ModelNullGroup, super().nulls)