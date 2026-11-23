# src/operation/computation/node/step/quadrant/southwest/worker.py

"""
Module: operation.computation.node.step.quadrant.southwest.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import QuadrantStepFunction


class SouthwestQuadrantNodeStepper(QuadrantNodeStepper):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Quadrant Space, using the linear functions:
                - V.x = U.x + x_step
                - V.y = (2 * slope * U.y) + slope

    Attributes:
        slope: int
        x_step: int

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        QuadrantNodeStepper
    """

    
    def __init__(
            self,
            slope: int = QuadrantStepFunction.SOUTHWEST.slope,
            x_step: int = QuadrantStepFunction.SOUTHWEST.x_step,
    ):
        """
        Args:
            slope: int
            x_step: int
        """
        super().__init__(slope=slope, x_step=x_step)