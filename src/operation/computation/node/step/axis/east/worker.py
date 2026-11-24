# src/operation/computation/node/step/axis/east/worker.py

"""
Module: operation.computation.node.step.axis.east.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDelta, Vector
from operation import AxisNodeStepper
from request import EastAxisProjectionRequest


class EastAxisNodeStepper(AxisNodeStepper[EastAxisProjectionRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Axis Space, by addition of a delta_vector
                - V.x = U.x + delta.x
                - V.y = U.x + delta.y

    Attributes:
        delta: Vector

    Provides:
        def execute(request: AxisMappingRequest) -> ComputationResult[Vector]

    Super Class:
        AxisNodeStepper
    """
    
    def __init__(self, delta: Vector = AxisDelta.EAST.vector):
        """
        Args:
            delta: Vector
        """
        super().__init__(delta=delta)
