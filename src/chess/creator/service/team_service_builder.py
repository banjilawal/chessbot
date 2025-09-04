from chess.creator.entity.factory.team_factory import TeamFactory
from chess.side.service import TeamService


class TeamServiceBuilder:

    @staticmethod
    def assemble() -> TeamService:
        teams = TeamFactory.assemble()
        return TeamService(teams)