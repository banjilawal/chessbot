from typing import List

from chess.coord import Coord


class DiagonalRay:
    
    @classmethod
    def compute(
            cls,
            start_x: int,
            end_x: int,
            x_step: int,
            end_y: int,
            slope: int
    ) -> List[Coord]:

#     self._compute_diagonal_ray(
#         start_x=0,
#         end_x=origin.column,
#         x_step=1,
#         end_y=origin.row,
#         slop=1,
#     ),