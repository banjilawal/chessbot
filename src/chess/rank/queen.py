from typing import List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant

if TYPE_CHECKING:
    from chess.rank.rank import Rank

from chess.rank.rank import Rank

class Queen(Rank):

    def __init__(self, name: str, letter: str, capture_value: int, territories: List[Quadrant]):

        from chess.motion.service.queen_motion_service import QueenMotionService
        super().__init__(name, letter, QueenMotionService(), capture_value, territories)
