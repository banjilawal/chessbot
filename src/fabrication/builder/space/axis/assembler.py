# src/fabrication/builder/space/axis/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from fabrication.builder import SpaceBuilder
from domain.metadata.blueprint import AxisBlueprint
from artifcat import BuildResult

from util import LoggingLevelRouter


T = TypeVar("T", bound="Axis")

class AxisBuilder(SpaceBuilder, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Axis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: AxisBlueprint,) -> BuildResult[Axis]

    Super Class:
        Builder
    """
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: [AxisBlueprint[T]],) -> BuildResult[T]:
        pass