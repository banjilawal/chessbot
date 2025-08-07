from typing import List

from chess.motion.abstract.motion_controller import MotionController
from chess.geometry.quadrant import Quadrant

from chess.motion.king.service.king_search_pattern import KingSearchPattern
from chess.motion.king.service.king_walk import KingWalk


class BishopMotionController(MotionController):

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant]
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=KingWalk(),
            search_pattern=KingSearchPattern(),
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

    # def __init__(
    #     self,
    #     name: str,
    #     letter: str,
    #     capture_value:
    #     int, number_per_team: int,
    #     territories: List[Quadrant]
    # ):
    #     super().__init__(
    #         name=name,
    #         letter=letter,
    #         walk=BishopWalk(),
    #         search_pattern=BishopSearchPattern(),
    #         capture_value=capture_value,
    #         territories=territories,
    #         number_per_team=number_per_team
    #     )

