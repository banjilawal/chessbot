# src/operation/computation/node/step/worker.py

"""
Module: operation.computation.node.step.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import ComputationResult
from controller import VectorComputationController
from fabrication import VectorBuilder
from operation import Computer
from request import ProjectionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="ProjectionRequest")

class SpaceNodeStepper(Computer[T], ABC, Generic[T]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Stepping function which gives the next vector in a Space.

    Attributes:
        vector_builder: VectorBuilder
        compute: VectorComputationController

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        Computer
    """
    _vector_builder: VectorBuilder
    _compute: VectorComputationController

    
    def __init__(
            self,
            vector_builder: Optional[VectorBuilder] | None = None,
            compute: Optional[VectorComputationController] | None = None,
    ):
        """
        Args:
            vector_builder: Optional[VectorBuilder]
            compute: Optional[VectorComputationController]
        """
        super().__init__()
        self._vector_builder = vector_builder or VectorBuilder()
        self._compute = compute or VectorComputationController()
        
    @property
    def vector_builder(self) -> VectorBuilder:
        return self._vector_builder
    
    @property
    def compute(self) -> VectorComputationController:
        return self._compute
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> ComputationResult:
        pass