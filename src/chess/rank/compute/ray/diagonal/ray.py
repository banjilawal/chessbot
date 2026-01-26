# src/chess/rank/compute/ray/diagonal/ray.py

"""
Module: chess.rank.compute.ray.diagonal.ray
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.rank import DiagonalRayComputationFailedException
from chess.system import BuildResult, ComputationResult, LoggingLevelRouter


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
            span: [Coord] =  List[Coord],
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
            *   span (List[Coord]):     List to append Coords to if they are not already in the list.
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        RAISES:
            *   DiagonalRayComputationFailedException
        """
        method = "DiagonalRay.compute"
        
        i = start_x
        j = (2 * slope * i) + slope
        while i < end_x and j < end_y:
            build_result = coord_service.builder.build(row=j, column=i)
            if build_result.is_failure:
                return BuildResult.failure(
                    DiagonalRayComputationFailedException(
                        message=f"{method}: {DiagonalRayComputationFailedException.DEFAULT_MESSAGE}",
                        ex=build_result.exception
                    )
                )
            if build_result.payload not in span:
                span.append(build_result.payload)
            i += x_step
            j = (2 * slope * i) + slope
        return ComputationResult.success(payload=span)