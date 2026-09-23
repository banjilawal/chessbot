# src/domain/metadata/manifest/strcture/register/manifest.py

"""
Module: domain.metadata.manifest.structure.register.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Register, StructureManifest, RegisterNullGroup, RegisterTypeUnion

T = TypeVar("T", bound="Register")

class RegisterManifest(StructureManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a Register's security lifecycle.

     Attributes:
        types: RegisterTypeUnion[T]
        nulls: RegisterNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: RegisterTypeUnion[T],
            nulls: RegisterNullGroup[T],
    ):
        """
        Args:
            types: RegisterTypeUnion[T]
            nulls: RegisterNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> RegisterTypeUnion[T]:
        return cast(RegisterTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> RegisterNullGroup:
        return cast(RegisterNullGroup, super().nulls)