# src/fabrication/builder/space/axis/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.metadata.blueprint import AxisBlueprint
from fabrication.builder import SpaceBuilder
from artifcat import BuildResult
from operation.toolkit import AxisBuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Axis")


class AxisBuilder(SpaceBuilder, Generic[T]):

    
    def __init__(self, builder_toolkit: AxisBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> AxisBuilderToolkit:
        return cast(AxisBuilderToolkit[T], super().builder_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisBlueprint[T]) -> BuildResult[T]:
        pass