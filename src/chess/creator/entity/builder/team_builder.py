
from chess.team.schema import TeamSchema
from chess.system.emitter import id_emitter
from chess.competitor.commander import Commander
from chess.side.team import Side


class TeamBuilder:

    @staticmethod
    def build(owner: Commander, config: TeamSchema) -> Side:
       print("build team got config", config)
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
#     teams: list[Team] = []
#     for config in TeamConfig:
#         commander = OwnerBuilder.build(id_emitter.commander_id)
#         team = TeamBuilder.build(commander, config)
#         print(team)
#         if team not in teams:
#             teams.append(team)
#     print(len(teams))
#
#     old_owwer = teams[0].commander
#     teams[0].commander = None
#     print(teams[0])
#
#     teams[0].commander = OwnerBuilder.build(id_emitter.commander_id)
#     print(teams[0])
#
#     team = TeamBuilder.build(old_owwer, TeamConfig.WHITE)
#     print(team)
#     print(old_owwer)
#
#
# if __name__ == "__main__":
#     main()