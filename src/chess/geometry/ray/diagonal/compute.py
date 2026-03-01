# src/chess/geometry/ray/diagonal/exception/wrapper.py

"""
Module: chess.geometry.ray.diagonal.exception.wrapper
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.geometry import CoordRay, DiagonalRayComputationException
from chess.system import ComputationResult, LoggingLevelRouter

class DiagonalRay:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            start_x: int,
            end_x: int,
            x_step: int,
            end_y: int,
            slope: int,
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  Iterate over the range of start_x to end_x with step x_step.
            2.  For each x find the y value using the slope.
            3.  Build a Coord from the x, y pair.
            4.  If the Coord is not in span, append it.
            5.  End the loop when x >= end_x and y >= end_y.
        PARAMETERS:
            *   start_x (int):          Starting x value. In practice, it will be occupant.current_position.column.
            *   end_x (int):            Ending x value. This will be either 0 or NUMBER_OF_COLUMNS - 1.
            *   x_step (int):           Step size for x. In practice, the magnitude will be 1,
                                        the sign may be negative.
            *   end_y (int):            Ending y value. This will be either 0 or NUMBER_OF_ROWS - 1 depending on the
                                        direction of travel.
            *   slope (int):            Slope of the diagonal. Used to find next y value.
            *   coord_service (CoordService):  CoordService instance.
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        RAISES:
            *   DiagonalRayComputationFailedException
        """
        method = "DiagonalRay.compute"
        points: List[Coord] = []
        
        i = start_x
        j = (2 * slope * i) + slope
        while i < end_x and j < end_y:
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
            if build_result.payload not in points:
               points.append(build_result.payload)
            i += x_step
            j = (2 * slope * i) + slope
            
        # Pop the first point and make it the origin.
        origin = points.pop(0) if points else None
        return ComputationResult.success(CoordRay(origin=origin, points=points))