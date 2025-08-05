from chess.factory.emit import id_emitter
from chess.factory.rank_factory import RankFactory
from chess.piece.piece import ChessPiece
from chess.player.human_player import HumanPlayer
from chess.player.player_config import PlayerConfig
from chess.rank.rank_config import RankConfig


class HumanPlayerBuilder:

    @staticmethod
    def build_player(name: str, player_config: PlayerConfig) -> HumanPlayer:
        """
        Builds a HumanPlayer instance and directly populates it with its initial pieces.
        This builder is fully responsible for creating all pieces for the team,
        avoiding delegation of piece creation to the Player object itself.
        """
        # 1. Create the HumanPlayer object
        player = HumanPlayer(
            player_id=id_emitter.player_id, # Get a unique ID for this team
            name=name,
            color=player_config.game_color
        )

        # 2. Directly create and assign pieces to this team.
        #    The piece counts are hardcoded here, as per your preference for direct control.

        # Create 2 Castles (Rooks)
        castle_rank = RankFactory.build_rank(RankConfig.CASTLE)
        for _ in range(2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=castle_rank)
            piece.player = player # The piece's setter adds it to team.pieces and rank.members

        # Create 2 Knights
        knight_rank = RankFactory.build_rank(RankConfig.KNIGHT)
        for _ in range(2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=knight_rank)
            piece.player = player

        # Create 2 Bishops
        bishop_rank = RankFactory.build_rank(RankConfig.BISHOP)
        for _ in range(2):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=bishop_rank)
            piece.player = player

        # Create 8 Pawns
        pawn_rank = RankFactory.build_rank(RankConfig.PAWN)
        for _ in range(8):
            piece = ChessPiece(piece_id=id_emitter.piece_id, rank=pawn_rank)
            piece.player = player

        # Create 1 King
        king_rank = RankFactory.build_rank(RankConfig.KING)
        piece = ChessPiece(piece_id=id_emitter.piece_id, rank=king_rank)
        piece.player = player

        # Create 1 Queen
        queen_rank = RankFactory.build_rank(RankConfig.QUEEN)
        piece = ChessPiece(piece_id=id_emitter.piece_id, rank=queen_rank)
        piece.player = player

        return player

    @staticmethod
    def build_players() -> list[HumanPlayer]:
        players: list[HumanPlayer] = []
        players.append(HumanPlayerBuilder.build_player("white", PlayerConfig.WHITE))
        players.append(HumanPlayerBuilder.build_player("black", PlayerConfig.BLACK))
        return players

def main():
    player = HumanPlayerBuilder.build_player("white", PlayerConfig.WHITE)
    players: list[HumanPlayer] = []
    players.append(player)
    players.append(HumanPlayerBuilder.build_player("black", PlayerConfig.BLACK))
    print(players)

if __name__ == "__main__":
    main()