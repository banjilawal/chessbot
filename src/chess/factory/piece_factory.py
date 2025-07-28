from typing import List


from chess.rank.rank_config import RankConfig
from chess.factory.emit import id_emitter
from chess.factory.rank_factory import RankFactory
from chess.piece.piece import Piece
from chess.rank.rank import Rank


class PieceFactory:


    @staticmethod
    def run_factory(ranks: List[Rank]) -> List[Piece]:
        pieces: List[Piece] = []

        for rank in ranks:
            pieces.extend(PieceFactory.build_rank_members(rank))
        return pieces


    @staticmethod
    def build_rank_members(rank: Rank) -> List[Piece]:
        rank_items: List[Piece] = []

        rank_config = RankConfig.find_config_by_class(rank=rank)
        for i in range(rank_config.number_per_player * 2):
            piece = Piece(id_emitter.piece_id, rank=rank)
            rank_items.append(piece)
        return rank_items


def main ():
    ranks: List[Rank] = RankFactory.run_factory()
    pieces = PieceFactory.run_factory(ranks)

    for piece in pieces:
        print(piece)
    for rank in ranks:
        print(len(rank.members))

if __name__ == "__main__":
    main()