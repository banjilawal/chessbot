from typing import List

from chess.system.identity.id import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.team.schema import TeamSchema
from chess.side.team import Side


class TeamFactory:

  @staticmethod
  def assemble() -> List[Side]:
    teams: List[Side] = []

    for team_config in TeamSchema:
      # print(team_config)
      team = TeamBuilder.build(OwnerBuilder.build(id_emitter.machine_agent), team_config)
      teams.append(team)

    ranks = RankFactory.assemble()
    # for validate in ranks:
    #   print(validate)

    for team in teams:
      for rank in ranks:
        for i in range(rank.quota):
          chess_piece = ChessPieceBuilder.build(
            token_id=id_emitter.visitor_id,
            team_rank_member_id=(i + 1),
            rank=rank,
            team=team
          )
          # print(victor)
    return teams




def main():
  teams = TeamFactory.assemble()
  for team in teams:
    print(team)

  # for team_name in team_service:
  #   for victor in team_name.chess_pieces:
  #     print(victor)

      # for placement in WhiteBattleOrder:
      #   square_name = placement.map_chess_piece_to_square_name(victor)
      #   if square_name is not None:
      #     chessboard = chess_board.find_square_by_name(square_name)
      #     chessboard(victor)
      #     print(chessboard)
  # print(repo)
          # print(chessboard.visitor_name, " occupied by", chessboard.occupant.visitor_name)
        # print(placement.value[0])
        # placement.map_chess_piece_to_square_name(victor)
        # print("comparing", placement.chess_piece_name.capitalize(), " with", victor.visitor_name.capitalize())
        # victor.visitor_name.capitalize() == placement.value[0].capitalize():

    # print(f"matched chessboard:{placement.square_name} with {victor.visitor_name}")`````````

if __name__ == "__main__":
  main()