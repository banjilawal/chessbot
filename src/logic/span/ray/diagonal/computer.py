# src/logic/span/ray/diagonal/computer.py

"""
Module: logic.span.ray/diagonal.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord, CoordService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.span import DiagonalRayComputationException, DiagonalRayFactors, Ray
from logic.vector import VectorService


class DiagonalRayComputer:
    """
    # BACKGROUND:
    1.  Consider the diagonal series: p_1(0,0), p_2(1,1), p_3(2,2), .., p_n(n,n). For any
            p_i, y_i = x_i.
        We want to find some invariant only in terms of x that will gives us all the ys.
    2.  Let us consider x in non-negative integers, {0, 1, 2,3,..,n}
        we now that
            x_i <= x_j < x_n.
    3.  The start of the X sequence is
            X_0 = 0,
            X_1 = 1,
            x_2 = 2
            x_3 = 3
       Which reveals: x_j = x_i + (j-i) But we want to express only in terms of x and restrict that i < j
            when i = 0, xo = x
            x_i = x_(i-1) + 1
    5. Since x_i = y_i, we can express the series in terms of x_(i-i)
            y_i = (x_(i-1) + delta_x) + x_(i-1)
            y_i = 2x_(i-1)
    6. In the quadrant(x<0, y>0) delta_x = -1.
    7. For thr quadrant (x<0, y>0) delta_x = 1.
    8. So for each quadrant we change the slope.

    # RESPONSIBILITIES:
    1.  Compute the spanning subset in the horizontal and vertical plane with no duplicates.
    2.  If the computation fails send an exception chain to the caller for error tracing.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            factors: DiagonalRayFactors,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Ray]:
        """
        # Action
            1.  Iterate over the range of start_x to end_x with step x_step.
            2.  For each x find the y value using the slope.
            3.  Build a Coord from the x, y pair.
            4.  If the Coord is not in span, append it.
            5.  End the loop when x >= end_x and y >= end_y.
            
        Args:
            factors: DiagonalRayFactors
            coord_service: CoordService
            
        Returns:
            ComputationResult[Ray]
            
        Raises:
            DiagonalRayComputationFailedException
        """
        method = f"{cls.__name__}.compute"
        
        points: List[Coord] = []
        
        i = factors.start_x
        j = (2 * factors.slope * i) + factors.slope
    
        while i < factors.end_x and j < factors.end_y:
            # Handle the case that the coord is not built.
            build_result = coord_service.builder.build(row=j, column=i)
            if build_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    DiagonalRayComputationException(
                        mthd=method,
                        op=DiagonalRayComputationException.OP,
                        msg=DiagonalRayComputationException.MSG,
                        err_code=DiagonalRayComputationException.ERR_CODE,
                        rslt_type=DiagonalRayComputationException.RSLT_TYPE,
                        ex=build_result.exception,
                    )
                )
            # Append the coord to points array if it's not already present.
            if build_result.payload not in points:
               points.append(build_result.payload)
            # Increment for the next step
            i += factors.x_step
            j = (2 * factors.slope * i) + factors.slope
        # --- Pop the first coord in the array as the ray's origins. ---#
        origin = points.pop(0)
        
        # --- Create the ray then send in the success result. ---#
        return ComputationResult.success(Ray(origin=origin, points=points))