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

from assurance import ChartDependency, StructValidatorToolkit
from domain import Chart, ChartManifest, ChartNullGroup, ChartTypeUnion

T = TypeVar("T", bound="Chart")


class ChartValidatorToolkit(StructValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: ChartWrapperDependency[T]
            metadata: ChartManifest[T]

    Provides:

    Super Class:
        StructValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: ChartDependency[T],
            metadata: ChartManifest[T],
    ):
        """
            wrapper: ChartWrapperDependency[T]
            metadata: ChartManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    
    @property
    def wrapper(self) -> ChartDependency[T]:
        return cast(ChartDependency, super().wrapper)
    
    @property
    def metadata(self) -> ChartManifest[T]:
        return cast(ChartManifest, super().metadata)
    
    @property
    def nulls(self) -> ChartNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> ChartTypeUnion[T]:
        return self.metadata.types