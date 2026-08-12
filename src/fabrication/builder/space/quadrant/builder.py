# src/fabrication/builder/space/quadrant/fabrication/builder.py

"""
Module: fabrication.builder.space.quadrant.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from fabrication.blueprint import Blueprint
from fabrication.builder import SpaceBuilder
from result import BuildResult
from toolkit import QuadrantBuilderToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantBuilder(SpaceBuilder, Generic[T]):

    
    def __init__(self, builder_toolkit: QuadrantBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @property
    def builder_toolkit(self) -> QuadrantBuilderToolkit:
        return cast(QuadrantBuilderToolkit[T], super().builder_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> BuildResult[T]:
        pass