from chess.creator.entity.factory.team_factory import TeamFactory
from chess.team.service import TeamService


class TeamServiceBuilder:

    @staticmethod
    def assemble() -> TeamService:
        teams = TeamFactory.assemble()
        return TeamService(teams)