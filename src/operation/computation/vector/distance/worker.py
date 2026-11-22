# src/operation/computation/vector/product/worker.py

"""
Module: operation.computation.vector.product.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector
from err import DistanceComputerException
from fabrication import ScalarBuilder
from operation import Computer
from request import DistanceRequest
from transit import DistanceComputationPermissionDispatcher

from util import LoggingLevelRouter


class DistanceComputer(VectorComputation[DistanceRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:
            permitter: Optional[DistanceComputerPermissionDispatcher]
            
    Provides:
        -   def execute(self, request: DistanceComputerRequest) -> ComputationResult[Vector]

    Super Class:
        Computation
    """
    _scalar_builder: ScalarBuilder
    
    def __init__(
            self,
            scalar_builder: Optional[ScalarBuilder] | None = None,
            permitter: Optional[DistanceComputationPermissionDispatcher] | None = None,
    ):
        """
        Args:
            scalar_builder: Optional[ScalarBuilder]
            permitter: Optional[DistanceComputerPermissionDispatcher]
        """
        super().__init__(permitter=permitter or DistanceComputationPermissionDispatcher())
        self._scalar_builder = scalar_builder or ScalarBuilder()
        
    @property
    def scalar_builder(self) -> ScalarBuilder:
        return self._scalar_builder
        
    @property
    def permitter(self) -> DistanceComputationPermissionDispatcher:
        return cast(DistanceComputationPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> ComputationResult[Vector]:
        pass

        