# src/chess/rank/compute/ray/diagonal/ray.py

"""
Module: chess.rank.compute.ray.diagonal.ray
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""
from typing import List

from chess.coord import Coord, CoordService
from chess.rank import DiagonalRay, PerpendicularSpanComputationFailedException
from chess.system import COLUMN_SIZE, ComputationResult, LoggingLevelRouter, ROW_SIZE
from chess.token import TokenService


class PerpendicularSpan:
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
          
        # Compute the ray in SW quadrant: [Po(0,0), Pn(origin.column, origin.row)]
        ray_computation_result = DiagonalRay.compute(
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
        span = ray_computation_result.payload
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(COLUMN_SIZE, 0)]
        ray_computation_result = DiagonalRay.compute(
            start_x=origin.column, end_x=COLUMN_SIZE, x_step=1, end_y=0, slope=1, span=span,
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
        span = ray_computation_result.payload
        # Compute the ray in NE quadrant: [Po(origin.column, 0), Pn(0, ROW_SIZE)]
        ray_computation_result = DiagonalRay.compute(
            start_x=origin.column, end_x=0, x_step=-1, end_y=ROW_SIZE, slope=-1, span=span,
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
            self._compute_diagonal_ray(
                start_x=origin.column,
                end_x=COLUMN_SIZE,
                x_step=1,
                end_y=ROW_SIZE,
                slope=-1,
                span=span,
            )
            return span
    
    class PerpendicularRay:
        
        @classmethod
        @LoggingLevelRouter.monitor
        def compute(
                cls,
                start_x: int,
                end_x: int,
                x_step: int,
                start_y: int,
                end_y: int,
                y_step: int,
                span: [Coord] = List[Coord],
                coord_service: CoordService = CoordService(),
        ) -> ComputationResult[List[Coord]]:
            method = "PerpendicularRay.compute"
            """
            # Action
                1.  Iterate over the range of start_x to end_x with step x_step.
                2.  For each x find the y value using the slope.
                3.  Build a Coord from the x, y pair.
                4.  If the Coord is not in span, append it.
                5.  End the loop when x >= end_x and y >= end_y.
            PARAMETERS:
                *   start_x (int):          Starting x value. In practice, it will be token.current_position.column.
                *   end_x (int):            Ending x value. This will be either 0 or COLUMN_SIZE - 1.
                *   x_step (int):           Step size for x. In practice, the magnitude will be 1,
                                            the sign may be negative.
                *   start_y (int):          Starting y value. In practice, it will be token.current_position.row.
                *   end_y (int):            Ending y value. This will be either 0 or ROW_SIZE - 1 depending on the
                                            direction of travel.
                *   y_step (int):           Step size for y. In practice, the magnitude will be 1,
                *   span (List[Coord]):     List to append Coords to if they are not already in the list.
            # RETURNS:
                *   ComputationResult[List[Coord]]:
                        - On failure: An exception.
                        - On success: List[Coord] in the payload.
            RAISES:
                *   DiagonalRayComputationFailedException
            """
            method = "Rank._compute_perpendicular_ray"
            i = start_x
            j = start_y
            
            while i < end_x and j < end_y:
                build_result = coord_service.builder.build(row=j, column=i)
                if build_result.is_failure:
                    return BuildResult.failure(
                        DiagonalRayComputationFailedException(
                            message=f"{method}: {PerpendicularRayComputationFailedException.DEFAULT_MESSAGE}",
                            ex=build_result.exception
                        )
                    )
                if build_result.payload not in span:
                    span.append(build_result.payload)
                i += x_step
                j += y_step
            return ComputationResult.success(payload=span)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            start_x: int,
            end_x: int,
            x_step: int,
            start_y: int,
            end_y: int,
            y_step: int,
            span: [Coord] = List[Coord],
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[List[Coord]]:
        method = "PerpendicularRay.compute"
        """
        # Action
        1.  Iterate over the range of start_x to end_x with step x_step.
        2.  For each x find the y value using the slope.
        3.  Build a Coord from the x, y pair.
        4.  If the Coord is not in span, append it.
        5.  End the loop when x >= end_x and y >= end_y.

        PARAMETERS:
            *   start_x (int):          Starting x value. In practice, it will be token.current_position.column.
            *   end_x (int):            Ending x value. This will be either 0 or COLUMN_SIZE - 1.
            *   x_step (int):           Step size for x. In practice, the magnitude will be 1,
                                        the sign may be negative.
            *   start_y (int):          Starting y value. In practice, it will be token.current_position.row.
            *   end_y (int):            Ending y value. This will be either 0 or ROW_SIZE - 1 depending on the
                                        direction of travel.
            *   y_step (int):           Step size for y. In practice, the magnitude will be 1,
            *   span (List[Coord]):     List to append Coords to if they are not already in the list.

        # RETURNS:
        List[Coord]

        RAISES:
        None
        """
        method = "Rank._compute_perpendicular_ray"
        i = start_x
        j = start_y
        
        while i < end_x and j < end_y:
            build_result = coord_service.builder.build(row=j, column=i)
            if build_result.is_failure:
                return BuildResult.failure(
                    DiagonalRayComputationFailedException(
                        message=f"{method}: {PerpendicularRayComputationFailedException.DEFAULT_MESSAGE}",
                        ex=build_result.exception
                    )
                )
            if build_result.payload not in span:
                span.append(build_result.payload)
            i += x_step
            j += y_step
        return ComputationResult.success(payload=span)


class Rank(ABC):
    """
    # ROLE: Computation

    # RESPONSIBILITIES:
    1.  Single-source-of-truth of Coords reachable from a Token's current position on the board.
    2.  Metadata for weighing edges in the GameGraph.
    3.  Hosting logic common to Rank subclasses.

    # PROVIDES:
    Rank

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   ransom (int)
        *   team_quota (int)
        *   designation(str)
        *   quadrants (List[Quadrant]):
    """
    _id: int
    _name: str
    _designation: str
    _ransom: int
    _team_quota: int
    _quadrants: list[Quadrant]
    _coord_service: CoordService
    _vector_service: VectorService
    
    def ray(self,
            id: int,
            name: str,
            designation: str,
            ransom: int,
            team_quota: int,
            quadrants: list[Quadrant],
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ):
        self._id = id
        self._name = name
        self._ransom = ransom
        self._team_quota = team_quota
        self._designation = designation
        self._quadrants = quadrants
        self._coord_service = coord_service
        self._vector_service = vector_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def compute_span(self, token: Token) -> [Coord]:
        """"""
        pass
 
        
        # return [
        #     self._compute_diagonal_ray(
        #         start_x=0,
        #         end_x=origin.column,
        #         x_step=1,
        #         end_y=origin.row,
        #         slop=1,
        #     ),
        #     self._compute_diagonal_ray(
        #         start_x=origin.column,
        #         end_x=COLUMN_SIZE,
        #         x_step=1,
        #         end_y=0,
        #         slope=1
        #     ),
        #     self._compute_diagonal_ray(
        #         start_x=origin.column,
        #         end_x=0,
        #         x_step=-1,
        #         end_y=ROW_SIZE,
        #         slope=-1
        #     ),
        #     self._compute_diagonal_ray(
        #         start_x=origin.column,
        #         end_x=COLUMN_SIZE,
        #         x_step=1,
        #         end_y=ROW_SIZE,
        #         slope=-1
        #     )
        # ]
    
    @LoggingLevelRouter.monitor
    def compute_perpendicular_span(self, token: Token) -> [Coord]:
        """
        # BACKGROUND:
        1.  Perpendicular relations will define a Cartesian plane with 4 quadrants.
        2.  In the X-plane, points are in the form: p_0(0,0), p_1(1,0), p_2(2,0), p_3(3,0), ...., p_n(n,0)
        3.  In the Y-plane, points are in the form: p_0(0,0), p_1(0,1), p_2(0,2), p_3(0,3), ...., p_n(0,n)
        4.  we can get the span by iterating over the quadrants with the in the range [0, BOARD_DIMENSION - 1]

        # Action
        1.  origin = token.current_position is the basis of the set.
        2.  Get points on each quadrant with a call to _compute_perpendicular_ray then append to a list.
        3.  Add origin to the span if it not already there.
        4.  Return the list.

        # PARAMETERS:
            *   token (Token): Single-source-of-truth for the basis of the span.

        # RETURNS:
        List[Coord]

        RAISES:
        None
        """
        method = "Rank.compute_perpendicular_span"
        
        origin = token.current_position
        span = [Coord]
        
        # Doing it this way avoids duplicates
        self._compute_perpendicular_ray(
            start_x=origin.column,
            end_x=origin.column,
            x_step=0,
            start_y=origin.row,
            end_y=origin.row,
            y_step=0,
            span=span
        )
        
        self._compute_perpendicular_ray(
            start_x=origin.column,
            end_x=COLUMN_SIZE,
            x_step=1,
            start_y=origin.row,
            end_y=origin.row,
            y_step=0,
            span=span,
        ),
        
        self._compute_perpendicular_ray(
            start_x=origin.column,
            end_x=origin.column,
            x_step=0,
            start_y=0,
            end_y=origin.row,
            y_step=1,
            span=span,
        )
        
        self._compute_perpendicular_ray(
            start_x=origin.column,
            end_x=origin.column,
            x_step=0,
            start_y=origin.row,
            end_y=COLUMN_SIZE,
            y_step=1,
            span=span,
        )
        return span
        
        # return [
        #     self._compute_perpendicular_ray(
        #         start_x=0,
        #         end_x=origin.column,
        #         x_step=1,
        #         start_y=origin.row,
        #         end_y=origin.row, y_step=0
        #     ),
        #     self._compute_perpendicular_ray(
        #         start_x=origin.column,
        #         end_x=COLUMN_SIZE,
        #         x_step=1,
        #         start_y=origin.row,
        #         end_y=origin.row,
        #         y_step=0
        #     ),
        #     self._compute_perpendicular_ray(
        #         start_x=origin.column,
        #         end_x=origin.column,
        #         x_step=0,
        #         start_y=0,
        #         end_y=origin.row,
        #         y_step=1
        #     ),
        #     self._compute_perpendicular_ray(
        #         start_x=origin.column,
        #         end_x=origin.column,
        #         x_step=0,
        #         start_y=origin.row,
        #         end_y=COLUMN_SIZE,
        #         y_step=1
        #     )
        # ].append(origin)