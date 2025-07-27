from typing import List


from chess.config.rank_config import RankConfig
from chess.factory.emit import id_emitter
from chess.factory.rank_builder import RankBuilder
from chess.piece.piece import Piece
from chess.player.player import Player
from chess.rank.bishop import Bishop
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.rank.pawn import Pawn
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.rank.rook import Rook


class PieceBuilder:

    @staticmethod
    def build(rank: Rank) -> List[Piece]:
        pieces: List[Piece] = []
        rank_config = RankConfig.find_config_by_class(rank=rank)
        for i in range(rank_config.number_per_player):
            print("i", i)
            piece = Piece(id_emitter.piece_id, rank=rank)
            print("id:" + str(piece.id) + " " + piece.label)
            pieces.append(piece)
        return pieces


def main ():
    rank = RankBuilder.build(RankConfig.BISHOP)
    pieces: List[Piece] = PieceBuilder.build(rank)
    for piece in pieces:
        print(piece)

if __name__ == "__main__":
    main()