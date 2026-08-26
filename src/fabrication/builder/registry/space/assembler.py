# src/fabrication/builder/space/reservoir/fabrication/builder.py

"""
Module: fabrication.builder.space.reservoir.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from fabrication.builder import Builder
from domain.metadata.blueprint import SpaceReservoirBlueprint
from artifcat import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="SpaceReservoir")

class SpaceReservoirBuilder(Builder, ABC, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SpaceReservoir instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(blueprint: [SpaceReservoirBlueprint[T]],,) -> BuildResult[T]

    Super Class:
        Builder
    """
    def __init__(self):
        super().__init__()
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: [SpaceReservoirBlueprint[T]],) -> BuildResult[T]:
        pass