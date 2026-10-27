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

from domain import NullWarningSet, Layer

T = TypeVar("T")

class DomainManifest(ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Model security lifecycle.

     Attributes:
        types: TypeUnion[T],
        nulls: NullWarningSet[T]

     Provides:

     Super Class:
     """
    
    _types: Layer[T]
    _nulls: NullWarningSet[T]
    
    def __init__(
            self,
            types: Layer[T],
            nulls: NullWarningSet[T]
    ):
        """
        Args:
            types: TypeUnion[T],
            nulls: NullWarningSet[T]
        """
        self._types = types
        self._nulls = nulls
        
    @property
    def types(self) -> Layer[T]:
        return self._types
    
    @property
    def nulls(self) -> NullWarningSet[T]:
        return self._nulls