# src/assurance/depend/toolkit/model/toolkit.py

"""
Module: assurance.depend.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import  LayerToolkit
from domain import Model, ModelManifest, ModelNullWarningSet, ModelLayer

T = TypeVar("T", bound="Model")


class ModelLayerToolkit(LayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
        helper: ServiceDependency[T]
        manifest: ModelManifest[T]

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    
    def __init__(
            self,
            dependency: ModelServiceDependency[T],
            manifest: ModelManifest[T],
    ):
        """
        Args:
            dependency: ServiceDependency[T]
            manifest: ModelManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    @property
    def dependency(self) -> ModelServiceDependency[T]:
        return cast(ModelServiceDependency[T], super().dependency)
    
    @property
    def manifest(self) -> ModelManifest[T]:
        return cast(ModelManifest[T], super().manifest)
    
    @property
    def nulls(self) -> ModelNullWarningSet[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> ModelLayer[T]:
        return self.manifest.types
    
