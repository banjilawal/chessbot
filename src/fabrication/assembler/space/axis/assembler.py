# src/assembler/space/axis/assembler.py

"""
Module: assembler.space.axis.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from fabrication.assembler import SpaceAssembler
from fabrication.blueprint import AxisBlueprint
from result import BuildResult

from util import LoggingLevelRouter


T = TypeVar("T", bound="Axis")

class AxisAssembler(SpaceAssembler, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Axis instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: AxisBlueprint,) -> BuildResult[Axis]

    Super Class:
        Assembler
    """
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: [AxisBlueprint[T]],) -> BuildResult[T]:
        pass