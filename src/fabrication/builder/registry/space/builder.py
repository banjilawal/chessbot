# src/fabrication/builder/registry/space/fabrication/builder.py

"""
Module: fabrication.builder.registry.space.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, Optional, TypeVar, cast

from fabrication.builder import Builder
from model import Vector

from result import BuildResult
from toolkit import MathToolkit, SpaceReservoirBuilderToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="SpaceReservoir")

class SpaceReservoirBuilder(Builder, Generic[T]):
    _math_toolkit: MathToolkit
    
    def __init__(
            self,
            builder_toolkit: Optional[SpaceReservoirBuilderToolkit] | None = None,
            math_toolkit: Optional[MathToolkit] | None = None,
    ):
        """
        Args:
            builder_toolkit: Optional[SpaceReservoirBuilderToolkit]
            math_toolkit: Optional[MathToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit or SpaceReservoirBuilderToolkit())
        self._math_toolkit = math_toolkit or MathToolkit()
        
    @property
    def builder_toolkit(self) -> SpaceReservoirBuilderToolkit:
        return cast(SpaceReservoirBuilderToolkit, super().builder_toolkit)
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> BuildResult[T]:
        pass
