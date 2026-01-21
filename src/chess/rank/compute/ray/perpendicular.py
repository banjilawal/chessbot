from typing import List

from chess.coord import Coord
from chess.system import ComputationResult, LoggingLevelRouter


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
     ) -> ComputationResult[List[Coord]]:
         span: List[Coord]
         
         return ComputationResult.success(span)
     

@LoggingLevelRouter.monitor
def _compute_perpendicular_ray(
        self,
        start_x: int,
        end_x: int,
        x_step: int,
        start_y: int,
        end_y: int,
        y_step: int,
        span: [Coord] = None,
):
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
        point = self.coord_service.build_coord(row=j, column=i)
        if point not in span:
            span.append(point)
        i += x_step
        j += y_step