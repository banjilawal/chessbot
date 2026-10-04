# src/domain/metadata/blueprint/struct/chart/blueprint.py

"""
Module: domain.metadata.blueprint.struct.chart.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Chart, StructBlueprint
from err import ChartNullException


T = TypeVar("T", bound="Chart")

class ChartBlueprint(StructBlueprint[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Chart.

     Attributes:
         domain_class: Type[T]
         domain_null_exception: ChartNullException

     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            domain_class: Type[T],
            domain_null_exception: ChartNullException,
    ):
        """
        Args:
            domain_class: Type[T]
            domain_null_exception: ChartNullException
        """
        super().__init__(
            domain_class=domain_class,
            domain_null_exception=domain_null_exception
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ChartNullException:
        return cast(ChartNullException, super().domain_null_exception)
    
    
