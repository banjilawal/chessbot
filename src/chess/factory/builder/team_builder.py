from chess.team import team_config
from chess.team.team import Team
from chess.team.team_config import TeamConfig


class TeamBuilder:

    @staticmethod
    def build(team_config: TeamConfig) -> Team:

        if team_config == TeamConfig.WHITE:
           return Team()

        return Team()


def main():
    team_builder = TeamBuilder.build(TeamConfig.WHITE)

if __name__ == "__main__":