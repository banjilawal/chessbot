# src/space/ray/computer/quadrant/space/ray.py

"""
Module: space.ray.computer.quadrant.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import QuadrantRayComputerException
from model import Vector, VectorRay
from space.ray import RayComputer
from result import ComputationResult
from space import KnightSpace


class QuadrantRayComputer(RayComputer[KnightSpace]):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce a ray of Vectors from the origin of an quadrant to its terminus.

    Attributes:
        space: Quadrant
        math_toolkit: MathToolkit

    Provides:
        -   def vector_ray() -> ComputationResult[List[Vector]]
        -   def coord_ray(self) -> ComputationResult[List[Coord]]

    Super Class:
        RayComputer
    """
    _space: KnightSpace
    
    def __init(self, space: KnightSpace):
        self._space = space
        
    @property
    def space(self) -> KnightSpace:
        return cast(KnightSpace, self.space)
    
    def execute(self, ) -> ComputationResult[VectorRay]:
        """
        Get the series of Vectors from the origin of the quadrant till its end.

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper does not finish its
                work before the loop invariant hits.
            2.  Otherwise, append the stepper's payload to the array and advance the cursor.
        Args:
        Returns:
            ComputationResult[VectorRay]
        Raises:
             QuadrantRayComputerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        ray: VectorRay = VectorRay()
        
        if self.space.is_empty:
            return ComputationResult.success(ray)
        
        # --- Set up for the loop ---#
        cursor = self.space.origin
        terminus = self.space.terminus
        
        # Less than is not a good choice for iterating through vectors.
        while cursor != terminus:
            ray.computer.add_point(cursor)
            
            # --- Request the vector from the space. ---#
            computation = self.space.stepper.next(current=cursor)
            
            # Handle the case that, request is not granted..
            if computation.is_failure:
                # Send the exception chain in the result.
                return ComputationResult.failure(
                    QuadrantRayComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=QuadrantRayComputerException.MSG,
                        err_code=QuadrantRayComputerException.ERR_CODE,
                        mthd_rslt_type=QuadrantRayComputerException.MTHD_RSLT_TYPE,
                        ex=computation.exception,
                    )
                )
            # Advance the cursor.
            cursor = cast(Vector, computation.payload)
            ray.computer.add_point(cursor)
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(ray)
