# src/fabrication/builder/space/fabrication/builder.py

"""
Module: fabrication.builder.space.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, Optional, TypeVar, cast

from fabrication.builder import Builder
from domain.model import Vector

from artifcat import BuildResult
from operation.toolkit import MathToolkit, SpaceBuilderToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")

class SpaceBuilder(Builder, Generic[T]):
    _math_toolkit: MathToolkit
    
    def __init__(
            self,
            builder_toolkit: Optional[SpaceBuilderToolkit] | None = None,
            math_toolkit: Optional[MathToolkit] | None = None,
    ):
        """
        Args:
            builder_toolkit: Optional[SpaceBuilderToolkit]
            math_toolkit: Optional[MathToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit or SpaceBuilderToolkit())
        self._math_toolkit = math_toolkit or MathToolkit()
        
    @property
    def builder_toolkit(self) -> SpaceBuilderToolkit:
        return cast(SpaceBuilderToolkit, super().builder_toolkit)
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> BuildResult[T]:
        pass
