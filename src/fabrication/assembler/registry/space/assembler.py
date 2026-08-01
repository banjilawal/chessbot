# src/assembler/space/reservoir/assembler.py

"""
Module: assembler.space.reservoir.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from fabrication.assembler import Assembler
from blueprint import SpaceReservoirBlueprint
from result import BuildResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="SpaceReservoir")

class SpaceReservoirAssembler(Assembler, ABC, Generic[T]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a SpaceReservoir instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(blueprint: [SpaceReservoirBlueprint[T]],,) -> BuildResult[T]

    Super Class:
        Assembler
    """
    def __init__(self):
        super().__init__()
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: [SpaceReservoirBlueprint[T]],) -> BuildResult[T]:
        pass