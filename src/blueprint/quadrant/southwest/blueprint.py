# src/blueprint/quadrant/southwest/blueprint.py

"""
Module: blueprint.quadrant.southwest.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import setting.board.dimension.config
from blueprint import QuadrantBlueprint
from model import Vector


class SouthwestQuadrantBlueprint(QuadrantBlueprint):
    X_STEP: int = -1
    SLOPE: int = 1
    TERMINUS: Vector = Vector(
        x=0,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    
    def __init__(
            self,
            x_step: int = X_STEP,
            slope: int = SLOPE,
            terminus: Vector = TERMINUS,
    ):
        super().__init__(x_step=x_step, slope=slope, terminus=terminus)
    
    