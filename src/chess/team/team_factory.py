from chess.common.config import ChessPieceConfig
from chess.common.emitter import id_emitter
from chess.figure.chess_piece import Pawn, Knight
from chess.team.chess_piece_builder import ChessPieceBuilder
from chess.team.team import Team
from podscape.constants import GameColor


def TeamBuilder():

    def __init__(self):
        pass

    def build_team(self, team_id: int, team_color: GameColor) -> Team:
        product = Team(team_id=team_id, color=team_color)

        for config in ChessPieceConfig:
            add_rank_members(team, config)
        return product

    def add_rank_memebers(self, team: Team, config: ChessPieceConfig):
        base_name = team.color + "_" + config.name
        for i in range config.number_of_members():
            name = base_name + "_" + str(i + 1)
            chess_piec


    def get_pawn_dictionary(team: Team):
        pawn_config = ChessPieceConfig.PAWN
        rank = pawn_config.get_rank()
        base_name = team.color + "_" + pawn_config.name
        pawn_dict = {}

        for i in pawn_config.number_per_team():
            key = i + 1
            name = base_name + "_" + key
            rank = i + 1
            chess_piece_id = id_emitter.chess_piece_id()
            pawn_dict[key] = Pawn(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
        return pawn_dict


    def get_knight_dictionary(team: Team):
        base_name = team.color + "_" + ChessPieceConfig.KNIGHT.name
        rank = ChessPieceBuildConfig.KNIGHT.rank()
        knight_dict = {}

        for i in ChessPieceConfig.KNIGHT.number_per_team():
            key = i + 1
            name = base_name + "_" + key
            chess_piece_id = id_emitter.chess_piece_id()
            knight_dict[key] = Knight(chess_piece_id=chess_piece_id, name=name, team=team, rank=rank)
        return knight_dict

