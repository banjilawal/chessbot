# src/span/king/span.py

"""
Module: span.king.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from _ast import List
from typing import cast

from model import King, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space.span import Span

from util import LoggingLevelRouter


class KingSpan(Span[King]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        bounds: KingBounds
        stepper: KingStepper

    Provides:
        -   destination_vectors(self) -> ComputationResult[VectorSet]

    Super Class:
        SpanningSet
    """

    
    def __init__(self, bounds: KingSpanBounds):
        """
        Args:
            bounds: KingBounds
            stepper: KingStepper
        """
        super().__init__(bounds=bounds)
    
    @property
    def bounds(self) -> KingSpanBounds:
        return cast(KingSpanBounds, self.bounds)
    

    @LoggingLevelRouter.monitor
    def compute_destinations(self) -> ComputationResult[VectorSet]:
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
                    KingSpanningSetException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KingSpanningSetException.MSG,
                        err_code=KingSpanningSetException.MSG,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    )
                )
            # On success cast and append to the solution set.
            solutions.append(cast(Vector, computation.payload))
        destination_vector_set = VectorSet(entries=tuple(solutions))
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(destination_vector_set)
        
    