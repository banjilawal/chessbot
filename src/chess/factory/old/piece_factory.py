from typing import List


from chess.rank.rank_config import RankConfig
from chess.factory.emit import id_emitter
from chess.factory.old.expired_rank_factory import RankFactoryAntiPattern
from chess.piece.piece import ChessPiece
from chess.rank.rank import Rank


class PieceFactory:


    @staticmethod
    def run_factory(ranks: List[Rank]) -> List[ChessPiece]:
        pieces: List[ChessPiece] = []

        for rank in ranks:
            pieces.extend(PieceFactory.build_rank_members(rank))
        return pieces


    @staticmethod
    def build_rank_members(rank: Rank) -> List[ChessPiece]:
        rank_items: List[ChessPiece] = []

        rank_config = RankConfig.find_config_by_class(rank=rank)
        for i in range(rank_config.number_per_player * 2):
            piece = ChessPiece(id_emitter.chess_piece_id, rank=rank)
            rank_items.append(piece)
        return rank_items


def main ():
    ranks: List[Rank] = RankFactoryAntiPattern.run_factory()
    pieces = PieceFactory.run_factory(ranks)

    for piece in pieces:
        print(piece)
    for rank in ranks:
        print(len(rank.members))

if __name__ == "__main__":
    main()