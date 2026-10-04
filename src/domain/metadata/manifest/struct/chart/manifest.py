# src/domain/metadata/manifest/strcture/chart/manifest.py

"""
Module: domain.metadata.manifest.struct.chart.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Chart, StructManifest, ChartNullGroup, ChartTypeUnion

T = TypeVar("T", bound="Chart")

class ChartManifest(StructManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Chart security lifecycle.

     Attributes:
        types: ChartTypeUnion[T]
        nulls: ChartNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: ChartTypeUnion[T],
            nulls: ChartNullGroup[T],
    ):
        """
        Args:
            types: ChartTypeUnion[T]
            nulls: ChartNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> ChartTypeUnion[T]:
        return cast(ChartTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> ChartNullGroup:
        return cast(ChartNullGroup, super().nulls)