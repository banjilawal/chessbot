from chess.token.model import Piece
from chess.rank.base import Rank

from chess.side.model import Side


class ChessPieceBuilder:


    @staticmethod
    def build(token_id: int, team_rank_member_id: int, rank: Rank, team: Side):

        name = team.letter.capitalize() + rank.letter.capitalize() + str(team_rank_member_id)
        if rank.letter == "K" or rank.letter == "Q":
            name = team.letter.capitalize() + rank.letter.capitalize()

        return Piece(
            token_id=token_id,
            name=name,
            rank=rank,
            team=team
        )
#
#
# def main():
#     motion = RankBuilder.build(RankConfig.BISHOP)
#     side = TeamBuilder.build(TeamConfig.WHITE)
#     captor = ChessPieceBuilder.build(id_emitter.chess_piece_id, 1, rank=motion, side=side)
#     print(captor)
#
# if __name__ == "__main__":
#     main()