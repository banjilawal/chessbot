# src/assembler/space/reservoir/quadrant/assembler.py

"""
Module: assembler.space.reservoir.quadrant.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.assembler import SpaceReservoirAssembler
from domain.metadata.blueprint import QuadrantReservoirBlueprint
from topology.registry import QuadrantReservoir
from artifcat.result import BuildResult

from util import LoggingLevelRouter



class QuadrantReservoirAssembler(SpaceReservoirAssembler[QuadrantReservoir]):
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
    def execute(self, blueprint: QuadrantReservoirBlueprint,) -> BuildResult[QuadrantReservoir]:
        return BuildResult.success(QuadrantReservoir(origin=blueprint.origin))