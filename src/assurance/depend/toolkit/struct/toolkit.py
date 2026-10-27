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

from assurance import StructDependency, LayerToolkit
from domain import Struct, StructManifest, StructNullWarningSet, StructLayer

T = TypeVar("T", bound="Struct")


class StructLayerToolkit(LayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: StructServiceDependency[T]
            manifest: StructManifest[T]

    Provides:

    Super Class:
        LayerToolkit
    """
    
    def __init__(
            self,
            dependency: StructDependency[T],
            manifest: StructManifest[T],
    ):
        """
            wrapper: StructServiceDependency[T]
            manifest: StructManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    
    @property
    def dependency(self) -> StructDependency[T]:
        return cast(StructDependency, super().dependency)
    
    @property
    def manifest(self) -> StructManifest[T]:
        return cast(StructManifest, super().manifest)
    
    @property
    def nulls(self) -> StructNullWarningSet[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> StructLayer[T]:
        return self.manifest.types