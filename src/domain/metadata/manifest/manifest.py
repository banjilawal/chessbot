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
    def type_union(self) -> TypeUnion[T]:
        return self._type_union
    
    @property
    def null_group(self) -> NullExceptionGroup:
        return self._null_group