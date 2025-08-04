from enum import Enum
from typing import List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant
from chess.motion.logic.bishop_reachable import BishopReachable
from chess.motion.logic.castle_reachable import CastleReachable
from chess.motion.logic.king_reachable import KingReachable
from chess.motion.logic.knight_reachable import KnightReachable
from chess.motion.logic.pawn_reachable import PawnReachable
from chess.motion.logic.reachable import Reachable
from chess.motion.search.bishop_search_pattern import BishopSearchPattern
from chess.motion.search.castle_search_pattern import CastleSearchPattern
from chess.motion.search.king_search_pattern import KingSearchPattern
from chess.motion.search.knight_search_pattern import KnightSearchPattern
from chess.motion.search.pawn_search_pattern import PawnSearchPattern
from chess.motion.search.search_pattern import SearchPattern
from chess.motion.service.bishop_motion_service import BishopMotionService
from chess.motion.service.castle_motion_service import CastleMotionService
from chess.motion.service.king_motion_service import KingMotionService
from chess.motion.service.knight_motion_service import KnightMotionService
from chess.motion.service.pawn_motion_service import PawnMotionService
from chess.motion.service.queen_motion_service import QueenMotionService
from chess.rank.rank import Rank

if TYPE_CHECKING:
    from chess.motion.service.motion_service import MotionService

class RankConfig(Enum):
    def __new__(
        cls,
        name: str,
        acronym,
        number_per_player: int,
        capture_value: int,
        territories: List[Quadrant],
        motion_service: MotionService = None,
    ):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._acronym = acronym
        obj._number_per_player = number_per_player
        obj._capture_value = capture_value
        obj._territories = territories
        obj._motion_service = motion_service
        return obj

    KING =(
        "King", "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W,Quadrant.NW],
        KingMotionService()
    )

    PAWN = (
        "Pawn", "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW], PawnMotionService()
    )

    KNIGHT = (
        "Knight", "N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW],
        KnightMotionService()
    )

    BISHOP = (
        "Bishop", "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW], BishopMotionService()
    )

    CASTLE = (
        "Castle", "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W], CastleMotionService()
    )

    QUEEN = (
        "Queen", "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW],
        QueenMotionService()
    )

    @property
    def acronym(self) -> str:
        return self._acronym

    @property
    def number_per_player(self) -> int:
        return self._number_per_player

    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> [Quadrant]:
        return self._territories.copy()

    @staticmethod
    def find_config_by_class(rank: Rank):
        print(f"Looking for config with name: {rank.name}")
        for config in RankConfig:
            print(f"Checking config: {config.value}")
            if config.value.upper() == rank.name.upper():
                return config
        return None


