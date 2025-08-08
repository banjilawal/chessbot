from chess.team.element.piece import ChessPiece
from chess.rank.rank import Rank

from chess.team.element.team import Team


class ChessPieceBuilder:


    @staticmethod
    def build(chess_piece_id: int, team_rank_member_id: int, rank: Rank, team: Team):

        name = team.letter.capitalize() + rank.letter.capitalize() + str(team_rank_member_id)
        if rank.letter == "K" or rank.letter == "Q":
            name = team.letter.capitalize() + rank.letter.capitalize()

        return ChessPiece(
            chess_piece_id=chess_piece_id,
            name=name,
            rank=rank,
            team=team
        )
#
#
# def main():
#     motion = RankBuilder.build(RankConfig.BISHOP)
#     team = TeamBuilder.build(TeamConfig.WHITE)
#     chess_piece = ChessPieceBuilder.build(id_emitter.chess_piece_id, 1, rank=motion, team=team)
#     print(chess_piece)
#
# if __name__ == "__main__":
#     main()