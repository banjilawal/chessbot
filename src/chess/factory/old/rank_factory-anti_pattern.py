from typing import List

from chess.rank.rank_config import RankConfig
from chess.rank.bishop import Bishop
from chess.motion.king.king_motion_controller import KingMotionController
from chess.motion.knight.knight_motion_controller import KnightMotionController
from chess.motion.pawn.pawn_motion_controller import PawnMotionController
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.rank.castle import Castle


class RankFactoryAntiPattern:

    @staticmethod
    def run_factory() -> List[Rank]:
        ranks: list[Rank] =  []
        for config in RankConfig:
            ranks.append(RankFactoryAntiPattern.build_rank(config))
        return ranks

    @staticmethod
    def build_rank(config: RankConfig) -> Rank:
        if config == RankConfig.KING:
            return KingMotionController(
                name=config.name,
                letter=config.letter,
                # motion_service=KingMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        if config == RankConfig.PAWN:
            return PawnMotionController(
                name=config.name,
                letter=config.letter,
                # motion_service=PawnMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        if config == RankConfig.KNIGHT:
            return KnightMotionController(
                name=config.name,
                letter=config.letter,
                # motion_service=KnightMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        if config == RankConfig.BISHOP:
            return Bishop(
                name=config.name,
                letter=config.letter,
                # motion_service=BishopMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        if  config == RankConfig.CASTLE:
            return Castle(
                name=config.name,
                letter=config.letter,
                # motion_service=CastleMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        if config == RankConfig.QUEEN:
            return Queen(
                name=config.name,
                letter=config.letter,
                # motion_service=QueenMotionService,
                capture_value=config.capture_value,
                territories=config.territories
            )
        raise ValueError(f"Invalid rank config: {config}")

def main ():
    ranks: List[Rank] = []
    for config in RankConfig:
        rank = RankFactoryAntiPattern.build_rank(config)
        ranks.append(rank)
        print(rank)
    print(f"num ranks {len(ranks)}")

    for rank in ranks:
        print(rank.name)

if __name__ == "__main__":
    main()