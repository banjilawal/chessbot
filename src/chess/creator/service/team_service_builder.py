from typing import List

from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.motion_controller_factory import MotionControllerFactory
from chess.creator.entity.factory.team_factory import TeamFactory
from chess.team.model.team import Team
from chess.team.team_service import TeamService


class TeamServiceBuilder:

    @staticmethod
    def assemble() -> TeamService:
        teams = TeamFactory.assemble()
        return TeamService(teams)