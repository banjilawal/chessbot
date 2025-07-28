from typing import List

from chess.common.game_color import GameColor
from chess.factory.emit import id_emitter
from chess.factory.piece_factory import PieceFactory
from chess.factory.rank_factory import RankFactory
from chess.piece.piece import Piece
from chess.player.human_player import HumanPlayer
from chess.player.player import Player
from chess.rank.rank import Rank


class PlayerFactory:

    @staticmethod
    def run_factory(player_names: List[str], pieces: List[Piece]) -> List[Player]:
        players: List[Player] = []

        white_player = HumanPlayer(player_id=id_emitter.player_id, name=player_names[0], color=GameColor.IVORY)
        black_player = HumanPlayer(player_id=id_emitter.player_id, name=player_names[1], color=GameColor.DARK_GRAY_3)

        for piece in pieces:
            if piece.id % 2 == 0:
                piece.player = white_player
            else:
                piece.player = black_player
            print(piece)

        players.append(white_player)
        players.append(black_player)
        return players

def main ():
    ranks = RankFactory.run_factory()
    pieces = PieceFactory.run_factory(ranks)
    players = PlayerFactory.run_factory(["white", "black"], pieces)

    for piece in players[0].pieces:
        print(piece)

if __name__ == "__main__":
    main()