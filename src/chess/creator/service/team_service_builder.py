from typing import List

from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.motion_controller_factory import MotionControllerFactory
from chess.team.model.team import Team
from chess.team.team_service import TeamService


class TeamServiceBuilder:

    @staticmethod
    def assemble() -> TeamService:
        teams = TeamServiceBuilder._build_teams()


    @staticmethod
    def _build_teams() -> List[Team]:
        teams: List[Team] = []

        for team_config in TeamConfig:
            print(team_config)
            team = TeamBuilder.repo_builder(team_config)
            teams.append(team)

        ranks = MotionControllerFactory.assemble()
        for rank in ranks:
            print(rank)

        for team in teams:
            for rank in ranks:
                for i in range(rank.number_per_player):
                    chess_piece = ChessPieceBuilder.repo_builder(
                        id_emitter.chess_piece_id,
                        (i + 1),
                        rank=rank,
                        team=team
                    )
                    # print(chess_piece)
        return teams