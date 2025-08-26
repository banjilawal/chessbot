from chess.token.piece import ChessPiece
from chess.rank.rank import Rank

from chess.team.team import Team


class ChessPieceBuilder:


    @staticmethod
    def build(token_id: int, team_rank_member_id: int, rank: Rank, team: Team):

        name = team.letter.capitalize() + rank.letter.capitalize() + str(team_rank_member_id)
        if rank.letter == "K" or rank.letter == "Q":
            name = team.letter.capitalize() + rank.letter.capitalize()

        return ChessPiece(
            token_id=token_id,
            name=name,
            rank=rank,
            team=team
        )
#
#
# def main():
#     motion = RankBuilder.build(RankConfig.BISHOP)
#     team = TeamBuilder.build(TeamConfig.WHITE)
#     captor = ChessPieceBuilder.build(id_emitter.chess_piece_id, 1, rank=motion, team=team)
#     print(captor)
#
# if __name__ == "__main__":
#     main()