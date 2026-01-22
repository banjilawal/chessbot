# src/chess/rank/compute/ray/diagonal/ray.py

"""
Module: chess.rank.compute.ray.diagonal.ray
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
from typing import List

from chess.coord import Coord, CoordService
from chess.rank import DiagonalRay, DiagonalSpanComputationFailedException
from chess.system import COLUMN_SIZE, ComputationResult, LoggingLevelRouter, ROW_SIZE

class DiagonalSpan:
    """
    # BACKGROUND:
    1. Consider a diagonal relation is: p_1(0,0), p_2(1,1), p_3(2,2), ...., p_n(n,n)
    2. For any p_i, y_i = x_i. So, once we know how x changes we can find the relation
       Let us consider x in non-negative integers, {0, 1, 2,3,....,n}
            x_n > x_j >= x_i.
    3. And,
            X_0 = 0,
            X_1 = 1,
            x_2 = 2
            x_3 = 3
       Looking at the indices we see x_j = x_i + (j-i)
    4. In terms of i only,
            x_i = x_(i-1) + (i - (i -1))
            x_i= x_(i-1) + delta_x
    5. Since x_i = y_i, we can express the series in terms of x_(i-i)
            y_i = (x_(i-1) + delta_x) + x_(i-1)
            y_i = 2x_(i-1)
    6. In the quadrant(x<0, y>0) delta_x = -1.
    7. For thr quadrant (x<0, y>0) delta_x = 1.
    8. So for each quadrant we change the slope.
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            origin: Coord,
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  origin = token.current_position is the basis of the set.
            2.  Get points on each quadrant with a call to _compute_diagonal_ray then append to a list.
            3.  Add origin to the span if it not already there.
            4.  Return the list.
        # PARAMETERS:
            *   token (Token): Single-source-of-truth for the basis of the span.
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   DiagonalRayComputationFailedException
        """
        method = "DiagonalSpan.compute"
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=origin)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
      
        # Get subset of the span in [N, E] quadrant: [Po(0,0), Pn(origin.column, origin.row)]
        ray_computation_result = DiagonalRay.compute(
            start_x=0, end_x=origin.column, x_step=1, end_y=origin.row, slope=1, span=List[Coord],
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # The unique span elements in the quadrant.
        span = ray_computation_result.payload
        
        # ge the subset of the span in [] quadrant: [Po(origin.column, 0), Pn(COLUMN_SIZE, 0)].
        ray_computation_result = DiagonalRay.compute(
            start_x=origin.column, end_x=COLUMN_SIZE, x_step=1, end_y=0, slope=1, span=span,
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # Get the current span.
        span = ray_computation_result.payload
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(0, ROW_SIZE)]
        ray_computation_result = DiagonalRay.compute(
            start_x=origin.column, end_x=0, x_step=-1, end_y=ROW_SIZE, slope=-1, span=span,
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(0, ROW_SIZE)]
        ray_computation_result = DiagonalRay.compute(
            start_x=origin.column, end_x=COLUMN_SIZE, x_step=1, end_y=ROW_SIZE, slope=-1,span=span,
        )
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # On search success send the span to the caller.
        return ComputationResult.success(span)