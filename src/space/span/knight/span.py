# src/span/knight/span.py

"""
Module: span.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _ast import List
from typing import cast

from container import VectorSet
from model import Vector
from result import ComputationResult
from space.span import KnightVectorBasis
from space.span.computer.span import DestinationSpanComputer

from util import LoggingLevelRouter


class KnightSpanner:
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        bounds: KnightBounds
        stepper: KnightStepper

    Provides:
        -   destination_vectors(self) -> ComputationResult[VectorSet]

    Super Class:
        SpanningSet
    """
    _span_computer: DestinationSpanComputer
    _basis: KnightVectorBasis = KnightVectorBasis()
    
    
    
    def __init__(self, origin: Vector):
        """
        Args:
            bounds: KnightBounds
            stepper: KnightStepper
        """
        self._basis = KnightVectorBasis(origin=origin)
    

    @LoggingLevelRouter.monitor
    def compute_destinations(self) -> ComputationResult[VectorSet]:
        method = f"{self.__class__.__name__}.destination_vectors"
        solutions: List[Vector] = []
        
        computation = self._span_computer.execute(basis=self._basis)
        if computation.is_failure:
            return ComputationResult.failure(computation.exception)
        destination_span = cast(VectorSet, computation.payload)
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(destination_span)
        
    