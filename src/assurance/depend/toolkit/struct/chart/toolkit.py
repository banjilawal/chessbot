# src/assurance/depend/toolkit/struct/chart.toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import ChartDependency, StructLayerToolkit
from domain import Chart, ChartManifest, ChartNullGroup, ChartTypeUnion

T = TypeVar("T", bound="Chart")


class ChartLayerToolkit(StructLayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: ChartServiceDependency[T]
            manifest: ChartManifest[T]

    Provides:

    Super Class:
        StructLayerToolkit
    """
    
    def __init__(
            self,
            dependency: ChartDependency[T],
            manifest: ChartManifest[T],
    ):
        """
            wrapper: ChartServiceDependency[T]
            manifest: ChartManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    
    @property
    def dependency(self) -> ChartDependency[T]:
        return cast(ChartDependency, super().dependency)
    
    @property
    def manifest(self) -> ChartManifest[T]:
        return cast(ChartManifest, super().manifest)
    
    @property
    def nulls(self) -> ChartNullGroup[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> ChartTypeUnion[T]:
        return self.manifest.types