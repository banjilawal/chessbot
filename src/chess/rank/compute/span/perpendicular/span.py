from typing import List

from chess.coord import Coord, CoordService
from chess.rank import PerpendicularRay, PerpendicularSpanComputationFailedException
from chess.system import COLUMN_SIZE, ComputationResult, LoggingLevelRouter


class PerpendicularSpan:
    """
    # BACKGROUND:
    1.  Perpendicular relations will define a Cartesian plane with 4 quadrants.
    2.  In the X-plane, points are in the form: p_0(0,0), p_1(1,0), p_2(2,0), p_3(3,0), ...., p_n(n,0)
    3.  In the Y-plane, points are in the form: p_0(0,0), p_1(0,1), p_2(0,2), p_3(0,3), ...., p_n(0,n)
    4.  we can get the span by iterating over the quadrants with the in the range [0, BOARD_DIMENSION - 1]
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
            2.  Get points on each quadrant with a call to _compute_perpendicular_ray then append to a list.
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
        method = "PerpendicularSpan.compute"
        
        # Handle the case that the coord is not certified safe.
        coord_validation = coord_service.validator.validate(candidate=origin)
        if coord_validation.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        
        # Get subset of the span in [N, E] quadrant: [Po(0,0), Pn(origin.column, origin.row)]
        ray_computation_result = PerpendicularRay.compute(
            start_x=0, end_x=origin.column, x_step=1, end_y=origin.row, slope=1, span=List[Coord],
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # The unique span elements in the quadrant.
        span = ray_computation_result.payload
        
        # ge the subset of the span in [] quadrant: [Po(origin.column, 0), Pn(COLUMN_SIZE, 0)].
        ray_computation_result = PerpendicularRay.compute(
            start_x=origin.column, end_x=origin.column, x_step=0, start_y=origin.row, end_y=origin.row, y_step=0, span=span
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # Get the current span.
        span = ray_computation_result.payload
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(0, ROW_SIZE)]
        ray_computation_result = PerpendicularRay.compute(
            start_x=origin.column, end_x=COLUMN_SIZE, x_step=1, start_y=origin.row, end_y=origin.row, y_step=0, span=span,
        )
        # Handle the case that the computation halted.
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(0, ROW_SIZE)]
        ray_computation_result = PerpendicularRay.compute(
            start_x=origin.column, end_x=origin.column, x_step=0, start_y=0, end_y=origin.row, y_step=1, span=span,
        )
        if ray_computation_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=ray_computation_result.exception
                )
            )
        # On search success send the span to the caller.
        return ComputationResult.success(span)