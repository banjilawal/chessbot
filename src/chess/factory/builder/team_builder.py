from chess.factory.emit import id_emitter
from chess.factory.rank_factory import RankFactory
from chess.team import team_config
from chess.team.team import Team
from chess.team.team_config import TeamConfig


class TeamBuilder:

    @staticmethod
    def build(team_id:int, config: TeamConfig, rank_factory: RankFactory) -> Team:
       team = Team(
           team_id=team_id,
           letter=config.letter,
           team_order=config.player_order,
           team_color=config.game_color,
           back_row_index=config.back_rank_index,
           pawn_row_index=config.pawn_rank_index,
           home_quadrant=config.quadrant
       )




def main():
    teams: list[Team] = []
    for config in TeamConfig:
        team = TeamBuilder.build(id_emitter.team_id, config)
        print(team)
        if team not in teams:
            teams.append(team)
    print(len(teams))


if __name__ == "__main__":
    main()