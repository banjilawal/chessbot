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

T = TypeVar("T")

class ObjectManifest(ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Model security lifecycle.

     Attributes:
        types: TypeUnion[T],
        nulls: NullExceptionGroup[T]

     Provides:

     Super Class:
     """
    
    _types: TypeUnion[T]
    _nulls: NullExceptionGroup[T]
    
    def __init__(
            self,
            types: TypeUnion[T],
            nulls: NullExceptionGroup[T]
    ):
        """
        Args:
            types: TypeUnion[T],
            nulls: NullExceptionGroup[T]
        """
        self._types = types
        self._nulls = nulls
        
    @property
    def types(self) -> TypeUnion[T]:
        return self._types
    
    @property
    def nulls(self) -> NullExceptionGroup[T]:
        return self._nulls