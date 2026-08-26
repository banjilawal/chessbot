# src/transit/dispatcher/builder/space/axis/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.space.axis.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.metadata.blueprint import AxisBlueprint
from transit.dispatcher.builder import SpaceBuildDispatcher
from artifcat import BuildResult
from operation.toolkit import AxisBuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Axis")


class AxisBuilder(SpaceBuildDispatcher, Generic[T]):

    
    def __init__(self, builder_toolkit: AxisBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> AxisBuilderToolkit:
        return cast(AxisBuilderToolkit[T], super().assembler)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisBlueprint[T]) -> BuildResult[T]:
        pass