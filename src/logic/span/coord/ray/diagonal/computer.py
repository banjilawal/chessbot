# src/logic/span/coord/ray/diagonal/computer.py

"""
Module: logic.span.coord.ray.diagonal.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord, CoordService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.span import ComputedNullRayDebugException, DiagonalRayComputationException, DiagonalRayFactors, CoordRay
from logic.vector import Vector, VectorService


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
    ) -> ComputationResult[CoordRay]:
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
            vector_service: VectorService
            
        Returns:
            ComputationResult[CoordRay]
            
        Raises:
            DiagonalRayComputationFailedException
        """
        method = f"{cls.__name__}.compute"
        
        members: List[Coord] = []
        # --- Use starting_x and the slope to build the cursor. ---#
        cursor_initialization_result = vector_service.builder.build(
            x=factors.start_x,
            y=cls._f_of_x(x=factors.start_x, slope=factors.slope),
        )
        # Handle the case that, the cursor is not built.
        if cursor_initialization_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                DiagonalRayComputationException(
                    mthd=method,
                    op=DiagonalRayComputationException.OP,
                    msg=DiagonalRayComputationException.MSG,
                    err_code=DiagonalRayComputationException.ERR_CODE,
                    rslt_type=DiagonalRayComputationException.RSLT_TYPE,
                    ex=cursor_initialization_result.exception,
                )
            )
        # --- The cursor has been initialized. ---#
        cursor = cursor_initialization_result.payload
        
        while cursor != factors.end_vector:
            # --- Convert the cursor vector into a coord. ---#
            conversion_result = coord_service.convert_vector_to_coord(cursor)
            
            # Handle the case that the conversion is unsuccessful.
            if conversion_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    DiagonalRayComputationException(
                        mthd=method,
                        op=DiagonalRayComputationException.OP,
                        msg=DiagonalRayComputationException.MSG,
                        err_code=DiagonalRayComputationException.ERR_CODE,
                        rslt_type=DiagonalRayComputationException.RSLT_TYPE,
                        ex=conversion_result.exception,
                    )
                )
            # Add the coord if it's not in the list
            if conversion_result.payload not in members:
                members.append(conversion_result.payload)
            
            # --- Update the cursor. ---#
            cursor_update_result = vector_service.builder.build(
                x=cursor.x,
                y=cls._f_of_x(x=cursor.x, slope=factors.slope),
            )
            # Handle the case that, the cursor is not updated.
            if cursor_update_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    DiagonalRayComputationException(
                        mthd=method,
                        op=DiagonalRayComputationException.OP,
                        msg=DiagonalRayComputationException.MSG,
                        err_code=DiagonalRayComputationException.ERR_CODE,
                        rslt_type=DiagonalRayComputationException.RSLT_TYPE,
                        ex=cursor_update_result.exception,
                    )
                )
            # Otherwise the cursor advances.
            cursor = cursor_update_result.payload
        # --- Do the clean steps when the loop finishes. ---#
        
        # Handle the case that there were no members in the ray.
        if len(members) == 0:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                DiagonalRayComputationException(
                    mthd=method,
                    op=DiagonalRayComputationException.OP,
                    msg=DiagonalRayComputationException.MSG,
                    err_code=DiagonalRayComputationException.ERR_CODE,
                    rslt_type=DiagonalRayComputationException.RSLT_TYPE,
                    ex=ComputedNullRayDebugException(
                        msg=ComputedNullRayDebugException.MSG,
                        err_code=ComputedNullRayDebugException.ERR_CODE,
                    )
                )
            )
        # --- Pop the first member to make it the ray's origin then, send the work product. ---#
        origin = members.pop(0)
        return ComputationResult.success(CoordRay(origin=origin, members=members))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _f_of_x(cls, x: int, slope: int) -> int:
        """
        Action:
            Calculate the y component of a vector using the line's
                *   slope
                *   its x component
        Args:
            x: int
            slope: int
        Returns:
            int
        Raises:
            None
        """
        return (2 * slope * x) + slope