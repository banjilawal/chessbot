from chess.factory.emit import id_emitter
from chess.factory.old.piece_factory import PieceFactory
from chess.factory.old.expired_rank_factory import RankFactoryAntiPattern
from chess.piece.piece import ChessPiece
from chess.player.human_player import HumanPlayer
from chess.player.player_config import PlayerConfig
from chess.rank.rank_config import RankConfig


class HumanPlayerBuilder:

    @staticmethod
    def build_player(name: str, player_config: PlayerConfig) -> HumanPlayer:
        player = object
        if player_config == PlayerConfig.WHITE:
            player = HumanPlayer(player_id=id_emitter.player_id, name=name, color=player_config.game_color)
        if player_config == PlayerConfig.BLACK:
            player = HumanPlayer(player_id=id_emitter.player_id, name=name, color=player_config.game_color)

        castle = RankFactoryAntiPattern.build_rank(RankConfig.CASTLE)
        for i in range (2):
            piece = ChessPiece(chess_piece_id=id_emitter.chess_piece_id, rank=castle)
            piece.player = player

        knight = RankFactoryAntiPattern.build_rank(RankConfig.KNIGHT)
        for i in range (2):
            piece = ChessPiece(chess_piece_id=id_emitter.chess_piece_id, rank=knight)
            piece.player = player

        bishop = RankFactoryAntiPattern.build_rank(RankConfig.BISHOP)
        for i in range (2):
            piece = ChessPiece(chess_piece_id=id_emitter.chess_piece_id, rank=bishop)
            piece.player = player

        pawn = RankFactoryAntiPattern.build_rank(RankConfig.PAWN)
        for i in range (8):
            piece = ChessPiece(chess_piece_id=id_emitter.chess_piece_id, rank=pawn)
            piece.player = player

        king = RankFactoryAntiPattern.build_rank(RankConfig.KING)
        piece = ChessPiece(chess_piece_id=id_emitter, rank=king)
        piece.player = player

        queen = RankFactoryAntiPattern.build_rank(RankConfig.QUEEN)
        piece = ChessPiece(chess_piece_id=id_emitter, rank=queen)
        piece.player = player

        return player

def main ():
    ranks = RankFactoryAntiPattern.run_factory()
    pieces = PieceFactory.run_factory(ranks)
    players = PlayerFactory.run_factory(["white", "black"], pieces)

    for piece in players[0].pieces:
        print(piece)

if __name__ == "__main__":
    main()