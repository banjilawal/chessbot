# src/assurance/depend/toolkit/struct/toolkit.py

"""
Module: assurance.depend.toolkit.struct.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import StructDependency, ValidatorToolkit
from domain import Struct, StructManifest, StructNullGroup, StructTypeUnion

T = TypeVar("T", bound="Struct")


class StructValidatorToolkit(ValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: StructWrapperDependency[T]
            metadata: StructManifest[T]

    Provides:

    Super Class:
        ValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: StructDependency[T],
            metadata: StructManifest[T],
    ):
        """
            wrapper: StructWrapperDependency[T]
            metadata: StructManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    
    @property
    def wrapper(self) -> StructDependency[T]:
        return cast(StructDependency, super().wrapper)
    
    @property
    def metadata(self) -> StructManifest[T]:
        return cast(StructManifest, super().metadata)
    
    @property
    def nulls(self) -> StructNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> StructTypeUnion[T]:
        return self.metadata.types