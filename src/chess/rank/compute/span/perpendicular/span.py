from typing import List

from chess.coord import Coord, CoordService
from chess.system import NUMBER_OF_COLUMNS, ComputationResult, LoggingLevelRouter
from chess.rank import PerpendicularRay, PerpendicularSpanComputationFailedException



class PerpendicularSpan:
    """
    # ROLE: Computation

    # BACKGROUND:
    The perpendicular
    1.  Perpendicular relations will define a Cartesian plane with 4 quadrants.
    2.  In the X-plane, points are in the form: p_0(0,0), p_1(1,0), p_2(2,0), p_3(3,0), ...., p_n(n,0)
    3.  In the Y-plane, points are in the form: p_0(0,0), p_1(0,1), p_2(0,2), p_3(0,3), ...., p_n(0,n)
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
            origin: Coord,
            points: List[Coord] = [],
            coord_service: CoordService = CoordService(),
            perpendicular_ray: PerpendicularRay = PerpendicularRay(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  If the origin does not pass its validation checks send an exception chain in the CalculationResult.
            2.  If perpendicular_ray fails when its computing either the northern, southern, eastern or western
                rays aof the origin, send an exception chain in the CalculationResult.
        # PARAMETERS:
            *   origin (Coord)
            *   points (List[Coord])
            *   coord_service (CoordService)
            *   perpendicular_ray (PerpendicularRay)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   PerpendicularSpanComputationFailedException
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
        # --- Compute rays in each quadrant pass points into next ray computation to prevent duplicates. ---#

        # Get subset of the span east of v(x=origin.column, y=origin.row)
        east_ray_result = perpendicular_ray.compute(
            start_x=origin.column,
            end_x=NUMBER_OF_COLUMNS - 1,
            x_step=1,
            start_y=origin.row,
            end_y=origin.row,
            y_step=0,
            span=points,
        )
        # Handle the case that the east_ray computation halted.
        if east_ray_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=east_ray_result.exception
                )
            )
        # Add unique points west of v(x=origin.column, y=origin.row) to get the horizontal spanning set.
        horizontal_ray_result = perpendicular_ray.compute(
            start_x=0,
            end_x=origin.column,
            x_step=1,
            start_y=origin.row,
            end_y=origin.row,
            y_step=0,
            span=east_ray_result.payload,
        )
        # Handle the case that the western ray computation halted.
        if horizontal_ray_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=horizontal_ray_result.exception
                )
            )
        # --- Compute rays in each quadrant pass points into next ray computation to prevent duplicates. ---#
        horizontal_span = horizontal_ray_result.payload

        # Add unique points north of v(x=origin.column, y=origin.row) to the horizontal spanning set.
        span_subset_result = perpendicular_ray.compute(
            start_x=origin.column,
            end_x=origin.column,
            x_step=0,
            start_y=origin.row,
            end_y=0,
            y_step=-1,
            span=horizontal_span,
        )
        # Handle the case that the computation halted.
        if span_subset_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=span_subset_result.exception
                )
            )
        # Add unique points south of v(x=origin.column, y=origin.row) to get complete perpendicular spanning set.
        perpendicular_span_result = perpendicular_ray.compute(
            start_x=origin.column,
            end_x=origin.column,
            x_step=0,
            start_y=origin.row,
            end_y=0,
            y_step=-1,
            span=span_subset_result.payload
        )
        if perpendicular_span_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                PerpendicularSpanComputationFailedException(
                    message=f"{method}: {PerpendicularSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=perpendicular_span_result.exception
                )
            )
        # On search success send the complete perpendicular spanning set to the caller.
        return ComputationResult.success(perpendicular_span_result.payload)