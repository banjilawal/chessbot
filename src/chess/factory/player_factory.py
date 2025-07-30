from typing import List

from chess.common.game_color import GameColor
from chess.factory.emit import id_emitter
from chess.factory.piece_factory import PieceFactory
from chess.factory.rank_factory import RankFactory
from chess.piece.piece import ChessPiece
from chess.player.human_player import HumanPlayer
from chess.player.player import Player
from chess.player.player_config import PlayerConfig
from chess.rank.knight import Knight
from chess.rank.rank import Rank
from chess.rank.rank_config import RankConfig


class HumanPlayerBuilder:

    @staticmethod
    def build_player(name: str, player_config: PlayerConfig) -> HumanPlayer:
        player = object
        if player_config == PlayerConfig.WHITE:
            player = HumanPlayer(player_id=id_emitter.player_id, name=name, color=player_config.game_color)
        if player_config == PlayerConfig.BLACK:
            player = HumanPlayer(player_id=id_emitter.player_id, name=name, color=player_config.game_color)

        castle = RankFactory.build_rank(RankConfig.CASTLE)
        for i in range (2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=castle)
            piece.player = player

        knight = RankFactory.build_rank(RankConfig.KNIGHT)
        for i in range (2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=knight)
            piece.player = player

        bishop = RankFactory.build_rank(RankConfig.BISHOP)
        for i in range (2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=bishop)
            piece.player = player

        pawn = RankFactory.build_rank(RankConfig.PAWN)
        for i in range (8):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=pawn)
            piece.player = player

        king = RankFactory.build_rank(RankConfig.KING)
        piece = ChessPiece(piece_id=id_emitter, rank=king)
        piece.player = player

        queen = RankFactory.build_rank(RankConfig.QUEEN)
        piece = ChessPiece(piece_id=id_emitter, rank=queen)
        piece.player = player

        return player

def main ():
    ranks = RankFactory.run_factory()
    pieces = PieceFactory.run_factory(ranks)
    players = PlayerFactory.run_factory(["white", "black"], pieces)

    for piece in players[0].pieces:
        print(piece)

if __name__ == "__main__":
    main()