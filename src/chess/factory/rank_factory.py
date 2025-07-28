from typing import List


from chess.rank.rank_config import RankConfig
from chess.rank.bishop import Bishop
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.rank.pawn import Pawn
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.rank.rook import Rook


class RankFactory:

    @staticmethod
    def run_factory() -> List[Rank]:
        ranks: list[Rank] =  []
        for config in RankConfig:
            ranks.append(RankFactory.build_rank(config))
        return ranks

    @staticmethod
    def build_rank(config: RankConfig) -> Rank:
        if config == RankConfig.KING:
            return King(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        if config == RankConfig.PAWN:
            return Pawn(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        if config == RankConfig.KNIGHT:
            return Knight(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        if config == RankConfig.BISHOP:
            return Bishop(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        if  config == RankConfig.ROOK:
            return Rook(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        if config == RankConfig.QUEEN:
            return Queen(name=config.name, acronym=config.acronym, capture_value=config.capture_value, territories=config.territories)
        raise ValueError(f"Invalid rank config: {config}")

def main ():
    ranks: List[Rank] = []
    for config in RankConfig:
        rank = RankFactory.build_rank(config)
        ranks.append(rank)
        print(rank)
    print(f"num ranks {len(ranks)}")

    for rank in ranks:
        print(rank.name)

if __name__ == "__main__":
    main()