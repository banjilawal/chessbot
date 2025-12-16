
from chess.team.schema import TeamSchema
from chess.system.identity.id import id_emitter
from chess.competitor.commander import Commander
from chess.side.team import Side


class TeamBuilder:

  @staticmethod
  def build(owner: Commander, config: TeamSchema) -> Side:
    print("builder team_name got config", config)
    team = Side(
      side_id=id_emitter.team_id,
      letter=config.letter,
      team_color=config.game_color,
      back_row_index=config.back_rank_index,
      pawn_row_index=config.pawn_rank_index,
      home_quadrant=config.quadrant,
      controller=owner
    )
    return team



#
# def main():
#   team_service: list[Team] = []
#   for config in TeamConfig:
#     player_agent = OwnerBuilder.builder(id_emitter.commander_id)
#     team_name = TeamBuilder.builder(player_agent, config)
#     print(team_name)
#     if team_name not in team_service:
#       team_service.append(team_name)
#   print(len(team_service))
#
#   old_owwer = team_service[0].player_agent
#   team_service[0].player_agent = None
#   print(team_service[0])
#
#   team_service[0].player_agent = OwnerBuilder.builder(id_emitter.commander_id)
#   print(team_service[0])
#
#   team_name = TeamBuilder.builder(old_owwer, TeamConfig.WHITE)
#   print(team_name)
#   print(old_owwer)
#
#
# if __name__ == "__main__":
#   main()