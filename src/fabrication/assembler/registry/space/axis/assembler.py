# src/assembler/space/reservoir/axis/assembler.py

"""
Module: assembler.space.reservoir.axis.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from fabrication.assembler import SpaceReservoirAssembler
from fabrication.blueprint import AxisReservoirBlueprint
from topology.registry import AxisReservoir
from result import BuildResult
from util import LoggingLevelRouter



class AxisReservoirAssembler(SpaceReservoirAssembler[AxisReservoir]):
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