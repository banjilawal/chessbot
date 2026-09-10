# src/domain/metadata/manifest/manifest.py

"""
Module: domain.metadata.manifest.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import NullExceptionGroup, TypeUnion

T = TypeVar("T", bound="Model")

class ObjectManifest(ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a Model's security lifecycle.

     Attributes:
        type_union: TypeUnion[T],
        null_group: NullExceptionGroup[T]

     Provides:

     Super Class:
     """
    
    _type_union: TypeUnion[T]
    _null_group: NullExceptionGroup[T]
    
    def __init__(
            self,
            type_union: TypeUnion[T],
            null_group: NullExceptionGroup[T]
    ):
        """
        Args:
            type_union: TypeUnion[T],
            null_group: NullExceptionGroup[T]
        """
        self._type_union = type_union
        self._null_group = null_group
        
    @property
    def types(self) -> TypeUnion[T]:
        return self._type_union
    
    @property
    def nulls(self) -> NullExceptionGroup:
        return self._null_group