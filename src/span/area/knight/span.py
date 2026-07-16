# src/span/area/knight/span.py

"""
Module: span.area.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _ast import List
from typing import cast

from model import Knight, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from span import KnightSpanBounds, Span, VectorSet
from util import LoggingLevelRouter


class KnightSpanningSet(Span[Knight]):
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
        -   def next(current: Vector) -> ComputationResult
        -   def northeast(origin: Vector) -> Knight
        -   def northwest(origin: Vector) -> Knight
        -   def southeast(origin: Vector) -> Knight
        -   def southwest(origin: Vector) -> Knight

    Super Class:
        Span

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """

    
    def __init__(self, bounds: KnightSpanBounds):
        """
        Args:
            bounds: KnightBounds
            stepper: KnightStepper
        """
        super().__init__(bounds=bounds)
    """INTERNAL: Use factory methods instead of direct constructor."""
    
    @property
    def bounds(self) -> KnightSpanBounds:
        return cast(KnightSpanBounds, self.bounds)
    

    @LoggingLevelRouter.monitor
    def destination_vectors(self) -> ComputationResult[VectorSet]:
        method = f"{self.__class__.__name__}.destination_vectors"
        solutions: List[Vector] = []
        
        # Handle the empty basis set first.
        if self.bounds.is_empty:
            return ComputationResult.success(VectorSet())
        
        origin = self.bounds.origin
        for delta in self.bounds.delta_vectors.entries:
            computation = self.math.add_vector.execute(
                register=VectorRegister(u=origin, v=delta)
            )
            # Handle the case that, the no solution is provided.
            if computation.is_failure:
                # Send an exception in chain in the result.
                ComputationResult.failure(
                    KnightSpanningSetException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KnightSpanningSetException.MSG,
                        err_code=KnightSpanningSetException.MSG,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    )
                )
            # On success cast and append to the solution set.
            solutions.append(cast(Vector, computation.payload))
        destination_vector_set = VectorSet(entries=tuple(solutions))
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(destination_vector_set)
        
    