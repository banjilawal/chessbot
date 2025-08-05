from typing import List

from chess.factory.builder.team_builder import TeamBuilder
from chess.factory.rank_factory import RankFactory
from chess.team.team import Team


class TeamFactory:

    @staticmethod
    def assemble(team_builder: TeamBuilder, rank_factory: RankFactory):
        teams: List[Team] = []
