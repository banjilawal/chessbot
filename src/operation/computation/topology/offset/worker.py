# src/operation/computation/worker.py

"""
Module: operation.computation.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ComputationResult
from fabrication import VectorBuilder
from operation import Computer, Worker
from request import ComputationRequest
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter

P = TypeVar("P", bound="ComputationPermissionDispatcher")
Q = TypeVar("Q", bound="ComputationRequest")


class OffsetTopology(TopologyComputer[OffsetTopologyRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ComputationRequest

    Attributes:
        vector_builder: VectorBuilder
        permitter: ComputationPermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> ComputationResult

    Super Class:
        Worker
    """
    _vector_builder: VectorBuilder
    
    def __init__(
            self, permitter: ComputationPermissionDispatcher,
            vector_builder: Optional[VectorBuilder] | None = None,
    ):
        """
        Args:
            permitter: ComputationPermissionDispatcher
        """
        super().__init__(permitter=permitter)
        self._vector_builder = vector_builder or VectorBuilder()
        
    @property
    def vector_builder(self) -> VectorBuilder:
        return self._vector_builder
    
    @property
    def permitter(self) -> ComputationPermissionDispatcher:
        return cast(ComputationPermissionDispatcher, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> ComputationResult:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            ComputationWorkerException
        """
        pass