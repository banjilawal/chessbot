from typing import List

from chess.system.id.emitter import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.team.schema import TeamSchema
from chess.competitor.commander import HumanCommander
from chess.competitor.commander import Commander
from chess.randomize.competitor import RandomName


class OwnerFactory:

  @staticmethod
  def assemble() -> List[Commander]:
    owners: List[Commander] = []

    wo = HumanCommander(competitor_id=id_emitter.person_id, name=RandomName.person())
    bo = HumanCommander(competitor_id=id_emitter.person_id, name=RandomName.person())

    wt = TeamBuilder.build(wo, TeamSchema.WHITE)
    bt = TeamBuilder.build(bo, TeamSchema.BLACK)

    ranks = RankFactory.assemble()
    for team in [wt, bt]:
      for rank in ranks:
        for i in range(rank.quota):
          chess_piece = ChessPieceBuilder.build(
            token_id=id_emitter.visitor_id,
            team_rank_member_id=(i + 1),
            rank=rank,
            team=team
          )
    owners.append(wo)
    owners.append(bo)
    return owners
    #
    #
    #
    # for team_config in TeamConfig:
    #   # print(team_config)
    #   team_name = TeamBuilder.build(OwnerBuilder.build(id_emitter.commander_id), team_config)
    #   teams.append(team_name)
    #
    #
    # # for validate in ranks:
    # #   print(validate)
    #
    # for team_name in teams:
    #   for validate in ranks:
    #     for i in range(validate.number_per_team):
    #       captor = ChessPieceBuilder.build(
    #         discovery_id=id_emitter.discovery_id,
    #         team_rank_member_id=(i + 1),
    #         validate=validate,
    #         team_name=team_name
    #       )
    #       # print(captor)
    # return teams




def main():
  owners = OwnerFactory.assemble()
  for owner in owners:
    print(owner, ",", len(owner.team_name.roster))

  # for team_name in teams:
  #   for captor in team_name.chess_pieces:
  #     print(captor)

      # for placement in PlacementChart:
      #   square_name = placement.map_chess_piece_to_square_name(captor)
      #   if square_name is not None:
      #     chessboard = chess_board.find_square_by_name(square_name)
      #     chessboard(captor)
      #     print(chessboard)
  # print(repo)
          # print(chessboard.visitor_name, " occupied by", chessboard.occupant.visitor_name)
        # print(placement.value[0])
        # placement.map_chess_piece_to_square_name(captor)
        # print("comparing", placement.chess_piece_name.capitalize(), " with", captor.visitor_name.capitalize())
        # captor.visitor_name.capitalize() == placement.value[0].capitalize():

    # print(f"matched chessboard:{placement.square_name} with {captor.visitor_name}")`````````

if __name__ == "__main__":
  main()