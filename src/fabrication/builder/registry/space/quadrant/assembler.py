# src/fabrication/builder/space/reservoir/quadrant/fabrication/builder.py

"""
Module: fabrication.builder.space.reservoir.quadrant.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import SpaceReservoirBuilder
from domain.metadata.blueprint import QuadrantReservoirBlueprint
from topology.registry import QuadrantReservoir
from artifcat import BuildResult

from util import LoggingLevelRouter



class QuadrantReservoirBuilder(SpaceReservoirBuilder[QuadrantReservoir]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a SpaceReservoir instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(blueprint: [SpaceReservoirBlueprint[T]],,) -> BuildResult[T]

    Super Class:
        Builder
    """
    def __init__(self):
        super().__init__()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: QuadrantReservoirBlueprint,) -> BuildResult[QuadrantReservoir]:
        return BuildResult.success(QuadrantReservoir(origin=blueprint.origin))