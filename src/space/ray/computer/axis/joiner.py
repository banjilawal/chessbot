# src/space/ray/computer/axis/space/ray.py

"""
Module: space.ray.computer.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from container import TargetVectorSet
from model import Vector
from result import ComputationResult
from space import Axis, LinearJoiner
from util import LoggingLevelRouter


class AxisJoiner(LinearJoiner[Axis]):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce a ray of Vectors from the origin of an axis to its terminus.

    Attributes:
        linear_space: Axis
        math_toolkit: MathToolkit

    Provides:
        -   def vector_ray() -> ComputationResult[List[Vector]]
        -   def coord_ray(self) -> ComputationResult[List[Coord]]

    Super Class:
        LinearJoiner
    """
    
    def __init__(self, linear_space: Axis):
        """
        Args:
            linear_space: Axis
        """
        super().__init__(linear_space=linear_space)
        
    @property
    def linear_space(self) -> Axis:
        return cast(Axis, self.linear_space)
    
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> ComputationResult[TargetVectorSet]:
        """
        Get the series of Vectors from the origin of the axis till its end.

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper does not finish its
                work before the loop invariant hits.
            2.  Otherwise, append the stepper's payload to the array and advance the cursor.
        Args:
        Returns:
            ComputationResult[VectorRay]
        Raises:
             AxisRayComputerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        axes: List[Axis] = [
            Axis.north_axis(origin),
            Axis.south_axis(origin),
            Axis.east_axis(origin),
            Axis.west_axis(origin),
        ]
        vector_sets: List[LinearTargetSet] = []
        
        for axis in axes:
            solution = axis.target_vectors()
            if solution.is_failure:
                # Send the exception chain in the result.
                return ComputationResult.failure(
                    AxisRayComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisRayComputerException.MSG,
                        err_code=AxisRayComputerException.ERR_CODE,
                        mthd_rslt_type=AxisRayComputerException.MTHD_RSLT_TYPE,
                        ex=solution.exception,
                    )
                )
            cleaned_set = cast(
                LinearTargetSet,
                solution.payload
            ).remove_root_destination()
            vector_sets.append(cleaned_set)
            
        vector_list: List[Vector] = []
        for item in vector_sets:
            vector_list.extend(item.to_list)
        return ComputationResult(
            TargetVectorSet(
                root=origin,
                entries=tuple(vector_list)
            )
        )
        
        
        # Deal with an empty Space.
        if self.linear_space.is_empty:
            return ComputationResult.success(ray)

        # --- Set up for the loop ---#
        cursor = self.linear_space.origin
        terminus = self.linear_space.terminus
        
        # Less than is not a good choice for iterating through vectors.
        while cursor != terminus:
            ray.computer.add_point(cursor)
            
            # --- Request the vector from the space. ---#
            computation = self.linear_space.stepper.next(current=cursor)
            
            # Handle the case that, request is not granted..
            if computation.is_failure:
                # Send the exception chain in the result.
                return ComputationResult.failure(
                    AxisRayComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisRayComputerException.MSG,
                        err_code=AxisRayComputerException.ERR_CODE,
                        mthd_rslt_type=AxisRayComputerException.MTHD_RSLT_TYPE,
                        ex=computation.exception,
                    )
                )
            # Advance the cursor.
            cursor = cast(Vector, computation.payload)
            ray.computer.add_point(cursor)
            
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(ray)
    
    def _helper(self, origin: Vector) -> ComputationResult[List[LinearTargetSet]]:
        north_axis = Axis.north_axis()