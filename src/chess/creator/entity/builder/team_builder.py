
from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.team.element.team import Team


class TeamBuilder:

    @staticmethod
    def build(config: TeamConfig) -> Team:
       print("build team got config", config)
       team = Team(
           team_id=id_emitter.team_id,
           letter=config.letter,
           team_order=config.player_order,
           team_color=config.game_color,
           back_row_index=config.back_rank_index,
           pawn_row_index=config.pawn_rank_index,
           home_quadrant=config.quadrant
       )
       return team


#
#
# def main():
#     teams: list[Team] = []
#     for config in TeamConfig:
#         team = TeamBuilder.build(config)
#         print(team)
#         if team not in teams:
#             teams.append(team)
#     print(len(teams))
#
#
# if __name__ == "__main__":
#     main()