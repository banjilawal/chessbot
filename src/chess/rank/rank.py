# src/chess/rank/rank.py

"""
Module: chess.rank.rank
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from abc import ABC, abstractmethod

from chess.coord import Coord, CoordService
from chess.piece import Piece
from chess.geometry import Quadrant
from chess.system import COLUMN_SIZE, LoggingLevelRouter, ROW_SIZE


class Rank(ABC):
    """
    # ROLE: Computation

    # RESPONSIBILITIES:
    1.  Single-source-of-truth of Coords reachable from a Piece's current position on the board.
    2.  Metadata for weighing edges in the GameGraph.
    3.  Hosting logic common to Rank subclasses.

    # PROVIDES:
    Rank

    # ATTRIBUTES:
        *   id (int):       Identifier for the subclass.
        *   name (str):     Common name of the rank.
        *   designation (str):   Chess designation
        *   ransom (int):   Value of ranks that can be captured.
        *   team_quota  (int):   Number of instances on a team.
        *   quadrants (List[Quadrant]):
    """
    _id: int
    _name: str
    _designation: str
    _ransom: int
    _team_quota: int
    _quadrants: list[Quadrant]
    _coord_service: CoordService
    
    def __init__(self,
            id: int,
            name: str,
            designation: str,
            ransom: int,
            team_quota: int,
            quadrants: list[Quadrant],
            coord_service: CoordService=CoordService(),
    ):
        self._id = id
        self._name = name
        self._ransom = ransom
        self._team_quota = team_quota
        self._designation = designation
        self._quadrants = quadrants
        self._coord_service = coord_service
    

    @abstractmethod
    @LoggingLevelRouter.monitor
    def compute_span(self, piece: Piece) -> [Coord]:
        """"""
        pass
    
    @LoggingLevelRouter.monitor
    def compute_diagonal_span(self, piece: Piece) -> [[Coord]]:
        """
        # BACKGROUND:
        1.  Consider a diagonal relation is: p_1(0,0), p_2(1,1), p_3(2,2), ...., p_n(n,n)
        2.  For any p_i, y_i = x_i. So, once we know how x changes we can find the relation
                Let us consider x in non-negative integers, {0, 1, 2,3,....,n}
                x_n > x_j >= x_i.
        3.  And,
                X_0 = 0,
                X_1 = 1,
                x_2 = 2
                x_3 = 3
            Looking at the indices we see x_j = x_i + (j-i)
        4.  In terms of i only,
                x_i = x_(i-1) + (i - (i -1))
                x_i= x_(i-1) + delta_x
        5.  Since x_i = y_i, we can express the series in terms of x_(i-i)
            y_i = (x_(i-1) + delta_x) + x_(i-1)
            y_i = 2x_(i-1)
        6.  In the quadrant(x<0, y>0) delta_x = -1.
        7.  For thr quadrant (x<0, y>0) delta_x = 1.
        8.  So for each quadrant we change the slope.
        
        # Action
        1.  origin = piece.current_position is the basis of the set.
        2.  Get points on each quadrant with a call to _compute_diagonal_ray then append to a list.
        3.  Add origin to the span
        4.  Return the list.

        PARAMETERS:
            *   piece (Piece): Single-source-of-truth for the basis of the span.
        
        # Returns:
        List[Coord]
        
        RAISES:
        None
        """
        origin = piece.current_position
        return [
            self._compute_diagonal_ray(
                start_x=0,
                end_x=origin.column,
                x_step=1,
                end_y=origin.row,
                slop=1
            ),
            self._compute_diagonal_ray(
                start_x=origin.column,
                end_x=COLUMN_SIZE,
                x_step=1,
                end_y=0,
                slope=1
            ),
            self._compute_diagonal_ray(
                start_x=origin.column,
                end_x=0,
                x_step=-1,
                end_y=ROW_SIZE,
                slope=-1
            ),
            self._compute_diagonal_ray(
                start_x=origin.column,
                end_x=COLUMN_SIZE,
                x_step=1,
                end_y=ROW_SIZE,
                slope=-1
            )
        ]
    
    @LoggingLevelRouter.monitor
    def _compute_diagonal_ray(
            self,
            start_x: int,
            end_x: int,
            x_step: int,
            end_y: int,
            slope: int
    ) -> [Coord]:
        """
        # Action
        1.  Iterate over the range of start_x to end_x with step x_step.
        2.  For each x find the y value using the slope.
        3.  Build a Coord from the x, y pair.
        4.  End the loop when x >= end_x and y >= end_y.
        5.  Return the list.

        PARAMETERS:
            *   piece (Piece): Single-source-of-truth for the basis of the span.

        # Returns:
        List[Coord]

        RAISES:
        None
        """
        ray = []
        i = start_x
        j = (2 * slope * i) + slope
        
        while i < end_x and j < end_y:
            ray.append(
                self.coord_service.build_coord(
                    row=j,
                    column=i
                )
            )
            i += x_step
            j = (2 * slope * i) + slope
        return ray
    
    @LoggingLevelRouter.monitor
    def compute_perpendicular_span(self, piece: Piece) -> [Coord]:
        """"""
        origin = piece.current_position
        return [
            self._compute_perpendicular_ray(
                start_x=0,
                end_x=origin.column,
                x_step=1,
                start_y=origin.row,
                end_y=origin.row, y_step=0
            ),
            self._compute_perpendicular_ray(
                start_x=origin.column,
                end_x=COLUMN_SIZE,
                x_step=1,
                start_y=origin.row,
                end_y=origin.row,
                y_step=0
            ),
            self._compute_perpendicular_ray(
                start_x=origin.column,
                end_x=origin.column,
                x_step=0,
                start_y=0,
                end_y=origin.row,
                y_step=1
            ),
            self._compute_perpendicular_ray(
                start_x=origin.column,
                end_x=origin.column,
                x_step=0,
                start_y=origin.row,
                end_y=COLUMN_SIZE,
                y_step=1
            )
        ]
    
    @LoggingLevelRouter.monitor
    def _compute_perpendicular_ray(
            self,
            start_x: int,
            end_x: int,
            x_step: int,
            start_y: int,
            end_y: int,
            y_step: int
    ) -> [Coord]:
        """"""
        i = start_x
        j = start_y
        
        points = [Coord]
        while i < end_x and j < end_y:
            points.append(
                self.coord_service.build_coord(
                    row=j,
                    column=i
                )
            )
            i += x_step
            j += y_step
        return points
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def designation(self) -> str:
        return self._designation
    
    @property
    def ransom(self) -> int:
        return self._ransom
    
    @property
    def quadrants(self) -> list[Quadrant]:
        return self._quadrants
    
    @property
    def team_quota(self) -> int:
        return self._team_quota
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Rank):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return (
            "bounds: {"
            f"id:{self._id}, "
            f"name:{self._name}, "
            f"designation:{self._designation}, "
            f"ransom:{self._ransom}, "
            f"team_quota:{self._team_quota}"
            "}"
        )