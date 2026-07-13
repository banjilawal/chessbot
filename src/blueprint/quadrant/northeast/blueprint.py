# src/blueprint/quadrant/northeast/blueprint.py

"""
Module: blueprint.quadrant.northeast.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import setting.board.dimension.config
from blueprint import QuadrantBlueprint
from model import Vector


class NortheastQuadrantBlueprint(QuadrantBlueprint):
    X_STEP: int = 1
    SLOPE: int = -1
    TERMINUS: Vector = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=0
    )
    
    def __init__(
            self,
            x_step: int = X_STEP,
            slope: int = SLOPE,
            terminus: Vector = TERMINUS,
    ):
        super().__init__(x_step=x_step, slope=slope, terminus=terminus)
    
    