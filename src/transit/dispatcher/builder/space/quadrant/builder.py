# src/transit/dispatcher/builder/space/quadrant/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.space.quadrant.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from transit.dispatcher.builder import SpaceBuilder
from artifcat import BuildResult
from operation.toolkit import QuadrantBuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantBuilder(SpaceBuilder, Generic[T]):

    
    def __init__(self, builder_toolkit: QuadrantBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> QuadrantBuilderToolkit:
        return cast(QuadrantBuilderToolkit[T], super().assembler)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass