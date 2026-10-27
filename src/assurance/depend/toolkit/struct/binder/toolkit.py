# src/assurance/depend/toolkit/struct/binder.toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import BinderServiceDependency, StructLayerToolkit
from domain import Binder, BinderManifest, BinderNullWarningSet, BinderLayer

T = TypeVar("T", bound="Binder")


class BinderLayerToolkit(StructLayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: BinderServiceDependency[T]
            manifest: BinderManifest[T]

    Provides:

    Super Class:
        StructLayerToolkit
    """
    
    def __init__(
            self,
            dependency: BinderServiceDependency[T],
            manifest: BinderManifest[T],
    ):
        """
            wrapper: BinderServiceDependency[T]
            manifest: BinderManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    
    @property
    def dependency(self) -> BinderServiceDependency[T]:
        return cast(BinderServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> BinderManifest[T]:
        return cast(BinderManifest, super().manifest)
    
    @property
    def nulls(self) -> BinderNullWarningSet[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> BinderLayer[T]:
        return self.manifest.types