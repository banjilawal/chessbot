# src/chess/rank/model/concrete/pawn/compute/attack/span.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.coord import Coord, CoordService
from chess.rank import DiagonalRay, DiagonalSpanComputationFailedException
from chess.system import NUMBER_OF_COLUMNS, ComputationResult, LoggingLevelRouter, NUMBER_OF_ROWS
from chess.vector import Vector


class PawnAttackSpan:
    """
    # BACKGROUND:
    1.  Consider the diagonal series: p_1(0,0), p_2(1,1), p_3(2,2), ...., p_n(n,n). For any
            p_i, y_i = x_i.
        We want to find some invariant only in terms of x that will gives us all the ys.
    2.  Let us consider x in non-negative integers, {0, 1, 2,3,....,n}
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
            origin: Coord,
            domain: List[Coord] = List[Coord],
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        """
        # Action
            1.  If the origin does not pass its validation checks send an exception chain in the CalculationResult.
            2.  If diagonal_ray fails when its computing either the northern, southern, eastern or western
                rays aof the origin, send an exception chain in the CalculationResult.
        # PARAMETERS:
            *   origin (Coord)
            *   points (List[Coord])
            *   coord_service (CoordService)
            *   diagonal_ray (DiagonalRay)
        # RETURNS:
            *   ComputationResult[List[Coord]]:
                    - On failure: An exception.
                    - On success: List[Coord] in the payload.
        # RAISES:
            *   DiagonalSpanComputationFailedException
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
        # --- Compute rays in each quadrant pass points into next ray computation to prevent duplicates. ---#
        
        # Get subset of the span in north-west of v(x=origin.column, y=origin.row). This is quadrant, Q1
        north_west_ray_result = DiagonalRay.compute(
            start_x=0,
            end_x=origin.column,
            x_step=1,
            end_y=origin.row,
            slope=1,
            span=domain,
        )
        # Handle the case that the northwestern computation does not produce a solution.
        if north_west_ray_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=north_west_ray_result.exception
                )
            )
        # Add unique points northeast of v(x=origin.column, y=origin.row) to get the northern spanning set.
        northern_ray_result = DiagonalRay.compute(
            start_x=origin.column,
            end_x=NUMBER_OF_ROWS - 1,
            x_step=1,
            end_y=0,
            slope=1, span=north_west_ray_result.payload,
        )
        # Handle the case that the northeastern ray computation does not produce a solution.
        if northern_ray_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=northern_ray_result.exception
                )
            )
        # --- Extract the northern spanning set and, pass it to the southern rays. ---#
        northern_span = northern_ray_result.payload
        
        span_subset_result = DiagonalRay.compute(
            start_x=origin.column,
            end_x=0,
            x_step=-1,
            end_y=NUMBER_OF_ROWS,
            slope=-1,
            span=northern_span,
        )
        # Handle the case that the southwest ray computation does not produce a solution.
        if span_subset_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=span_subset_result.exception
                )
            )
        # Add unique points southwest of v(x=origin.column, y=origin.row) to get complete diagonal spanning set.
        diagonal_span_result = DiagonalRay.compute(
            start_x=origin.column,
            end_x=NUMBER_OF_COLUMNS - 1,
            x_step=1,
            end_y=NUMBER_OF_ROWS - 1,
            slope=-1,
            span=span_subset_result.payload,
        )
        # Handle the case that the southeastern ray computation does not produce a solution.
        if diagonal_span_result.is_failure:
            # On failure return the exception chain
            return ComputationResult.failure(
                DiagonalSpanComputationFailedException(
                    message=f"{method}: {DiagonalSpanComputationFailedException.DEFAULT_MESSAGE}",
                    ex=diagonal_span_result.exception
                )
            )
        # On search success send the span to the caller.
        return ComputationResult.success(diagonal_span_result.payload)