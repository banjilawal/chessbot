# src/fabrication/builder/space/reservoir/axis/fabrication/builder.py

"""
Module: fabrication.builder.space.reservoir.axis.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import SpaceReservoirBuilder
from domain.metadata.blueprint import AxisReservoirBlueprint
from topology.registry import AxisReservoir
from artifcat import BuildResult
from util import LoggingLevelRouter



class AxisReservoirBuilder(SpaceReservoirBuilder[AxisReservoir]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a SpaceReservoir instance from the safe blueprint.

    Attributes:

    Provides:
        - def execute(blueprint: [SpaceReservoirBlueprint[T]],,) -> BuildResult[T]

    Super Class:
        Builder
    """
    def __init__(self):
        super().__init__()
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisReservoirBlueprint,) -> BuildResult[AxisReservoir]:
        return BuildResult.success(AxisReservoir(origin=blueprint.origin))