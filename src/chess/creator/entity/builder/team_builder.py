
from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.owner.owner import Owner
from chess.team.team import Team


class TeamBuilder:

    @staticmethod
    def build(owner: Owner, config: TeamConfig) -> Team:
       print("build team got config", config)
       team = Team(
           team_id=id_emitter.team_id,
           letter=config.letter,
           team_color=config.game_color,
           back_row_index=config.back_rank_index,
           pawn_row_index=config.pawn_rank_index,
           home_quadrant=config.quadrant,
           owner=owner
       )
       return team




def main():
    teams: list[Team] = []
    for config in TeamConfig:
        owner = OwnerBuilder.build(id_emitter.owner_id)
        team = TeamBuilder.build(owner, config)
        print(team)
        if team not in teams:
            teams.append(team)
    print(len(teams))

    old_owwer = teams[0].owner
    teams[0].owner = None
    print(teams[0])

    teams[0].owner = OwnerBuilder.build(id_emitter.owner_id)
    print(teams[0])

    team = TeamBuilder.build(old_owwer, TeamConfig.WHITE)
    print(team)
    print(old_owwer)


if __name__ == "__main__":
    main()