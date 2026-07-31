# src/assembler/space/reservoir/axis/assembler.py

"""
Module: assembler.space.reservoir.axis.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import Assembler
from blueprint import AxisReservoirBlueprint
from result import BuildResult
from space import AxisReservoir
from util import LoggingLevelRouter



class AxisReservoirAssembler(Assembler[AxisReservoir]):
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
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisReservoirBlueprint,) -> BuildResult[AxisReservoir]:
        return BuildResult.success(AxisReservoir(origin=blueprint.origin))