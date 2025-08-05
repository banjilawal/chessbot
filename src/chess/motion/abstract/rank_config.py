from enum import Enum
from typing import List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant

from chess.motion.bishop.service.bishop_motion_service import BishopMotionService
from chess.motion.castle.service.castle_motion_service import CastleMotionService
from chess.motion.king.service.king_motion_service import KingMotionService
from chess.motion.knight.service.knight_motion_service import KnightMotionService
from chess.motion.pawn.service.pawn_motion_service import PawnMotionService
from chess.motion.queen.service.queen_motion_service import QueenMotionService
from chess.motion.abstract.motion_controller import MotionController

if TYPE_CHECKING:
    from chess.motion.abstract.motion_service import MotionService

class RankConfig(Enum):
    def __new__(
        cls,
        name: str,
        letter,
        number_per_player: int,
        capture_value: int,
        territories: List[Quadrant],
        motion_service: 'MotionService',
    ):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._letter = letter
        obj._number_per_player = number_per_player
        obj._capture_value = capture_value
        obj._territories = territories
        obj._motion_service = motion_service
        return obj

    KING =(
        "KingMotionController", "K", 1, 0,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W,Quadrant.NW],
        KingMotionService()
    )

    PAWN = (
        "PawnMotionController", "P", 8, 1, [Quadrant.NE, Quadrant.SE, Quadrant.NW, Quadrant.SW], PawnMotionService()
    )

    KNIGHT = (
        "KnightMotionController", "N", 2, 3, [Quadrant.N, Quadrant.NE, Quadrant.NW, Quadrant.E, Quadrant.SE, Quadrant.SW],
        KnightMotionService()
    )

    BISHOP = (
        "Bishop", "B", 2, 3, [Quadrant.NE, Quadrant.NW, Quadrant.SE, Quadrant.SW], BishopMotionService()
    )

    CASTLE = (
        "CastleMotionController", "C", 2, 5, [Quadrant.N, Quadrant.S, Quadrant.E, Quadrant.W], CastleMotionService()
    )

    QUEEN = (
        "Queen", "Q", 1, 9,
        [Quadrant.N, Quadrant.NE, Quadrant.E, Quadrant.SE, Quadrant.S, Quadrant.SW, Quadrant.W, Quadrant.NW],
        QueenMotionService()
    )

    @property
    def letter(self) -> str:
        return self._letter

    @property
    def number_per_player(self) -> int:
        return self._number_per_player

    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories

    @property
    def motion_service(self) -> 'MotionService':
        return self._motion_service

    @staticmethod
    def find_config_by_class(rank: MotionController):
        print(f"Looking for config with name: {rank.name}")
        for config in RankConfig:
            print(f"Checking config: {config.value}")
            if config.value.upper() == rank.name.upper():
                return config
        return None


