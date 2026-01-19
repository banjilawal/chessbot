from chess.token.piece import Piece
from chess.rank.rank import Rank

from chess.side.team import Side


class ChessPieceBuilder:


  @staticmethod
  def build(token_id: int, team_rank_member_id: int, rank: Rank, team: Side):

    name = team.designation.capitalize() + rank.designation.capitalize() + str(team_rank_member_id)
    if rank.designation == "K" or rank.designation == "Q":
      name = team.designation.capitalize() + rank.designation.capitalize()

    return Piece(
      token_id=token_id,
      name=name,
      rank=rank,
      team=team
    )
#
#
# def main():
#   motion = RankFactory.builder(RankConfig.BISHOP)
#   team_name = TeamBuilder.builder(TeamConfig.WHITE)
#   victor = ChessPieceBuilder.builder(id_emitter.chess_piece_id, 1, validate=motion, team_name=team_name)
#   print(victor)
#
# if __name__ == "__main__":
#   main()