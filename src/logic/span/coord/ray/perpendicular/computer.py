# src/logic/span/coord/ray/perpendicular/computer.py

"""
Module: logic.span.coord.ray.perpendicular.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.vector import VectorService
from logic.coord import Coord, CoordService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.span import (
    ComputedNullRayDebugException, PerpendicularRayComputationException, PerpendicularRayFactors, CoordRay
)

class PerpendicularRayComputer:
    """
    # ROLE: Computation

    # BACKGROUND:
    The perpendicular domain is defined by relations in the Cartesian plane.
        #   The X-Plane:
                *   Given a range of ith-points where i = [0 < i < N] and for some c
                        p_i = p(x_(i-1), y_c)) = p(x_i, y_i)
                *   These are points north and south of  p_c
        #   The Y-Plane:
                *   Given a range of ith-points where i = [0 < i < N] and for some c
                        p_i = p(x_c, y_(i-1) + 1) = p(x_i, y_i)
                *   These are points north and south of  p_c
    4.  we can get the span by iterating over the quadrants with the in the range [0, BOARD_DIMENSION - 1]

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
            factors: PerpendicularRayFactors,
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
            coord_service: CoordService
            vector_service: VectorService
            factors: PerpendicularRayFactors
            
        Returns:
            ComputationResult[CoordRay]
            
        Raises:
            PerpendicularRayComputationException
        """
        method = f"{cls.__name__}.compute"
        

        members: List[Coord] = []
        cursor = factors.start_vector
        
        while cursor != factors.end_vector:
            # --- Convert the cursor vector into a coord. ---#
            conversion_result = coord_service.convert_vector_to_coord(cursor)
            
            # Handle the case that the conversion is unsuccessful.
            if conversion_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    PerpendicularRayComputationException(
                        mthd=method,
                        op=PerpendicularRayComputationException.OP,
                        msg=PerpendicularRayComputationException.MSG,
                        err_code=PerpendicularRayComputationException.ERR_CODE,
                        rslt_type=PerpendicularRayComputationException.RSLT_TYPE,
                        ex=conversion_result.exception,
                    )
                )
            # --- Add the coord if it's not in the list, then advance the cursor. ---#
            if conversion_result.payload not in members:
                members.append(conversion_result.payload)
            cursor_update_result = vector_service.add_vectors([cursor, factors.delta])
            
            # Handle the case that, the cursor is not updated.
            if cursor_update_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    PerpendicularRayComputationException(
                        mthd=method,
                        op=PerpendicularRayComputationException.OP,
                        msg=PerpendicularRayComputationException.MSG,
                        err_code=PerpendicularRayComputationException.ERR_CODE,
                        rslt_type=PerpendicularRayComputationException.RSLT_TYPE,
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
                PerpendicularRayComputationException(
                    mthd=method,
                    op=PerpendicularRayComputationException.OP,
                    msg=PerpendicularRayComputationException.MSG,
                    err_code=PerpendicularRayComputationException.ERR_CODE,
                    rslt_type=PerpendicularRayComputationException.RSLT_TYPE,
                    ex=ComputedNullRayDebugException(
                        msg=ComputedNullRayDebugException.MSG,
                        err_code=ComputedNullRayDebugException.ERR_CODE,
                    )
                )
            )
        # --- Pop the first member to make it the ray's origin then, send the work product. ---#
        origin = members.pop(0)
        return ComputationResult.success(CoordRay(origin=origin, members=members))
 