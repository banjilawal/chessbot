from typing import List


from chess.config.rank_config import RankConfig
from chess.factory.emit import id_emitter
from chess.factory.rank_factory import RankFactory
from chess.piece.piece import Piece
from chess.player.player import Player
from chess.rank.bishop import Bishop
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.rank.pawn import Pawn
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.rank.rook import Rook


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

        print(f"{rank.name} has {len(rank.members)} members")
        rank_config = RankConfig.find_config_by_class(rank=rank)
        for i in range(rank_config.number_per_player * 2):
            piece = Piece(id_emitter.piece_id, rank=rank)
            print("id:" + str(piece.id) + " " + str(piece.label))
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