
from chess.team.schema import TeamSchema
from chess.system.identity.id import id_emitter
from chess.competitor.commander import Commander
from chess.side.team import Side


class TeamBuilder:

  @staticmethod
  def build(owner: Commander, config: TeamSchema) -> Side:
    print("build team_name got config", config)
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
#   teams: list[Team] = []
#   for config in TeamConfig:
#     agent = OwnerBuilder.build(id_emitter.commander_id)
#     team_name = TeamBuilder.build(agent, config)
#     print(team_name)
#     if team_name not in teams:
#       teams.append(team_name)
#   print(len(teams))
#
#   old_owwer = teams[0].agent
#   teams[0].agent = None
#   print(teams[0])
#
#   teams[0].agent = OwnerBuilder.build(id_emitter.commander_id)
#   print(teams[0])
#
#   team_name = TeamBuilder.build(old_owwer, TeamConfig.WHITE)
#   print(team_name)
#   print(old_owwer)
#
#
# if __name__ == "__main__":
#   main()