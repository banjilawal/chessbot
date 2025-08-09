from chess.config.placement_chart import PlacementChart
from chess.creator.service.arena_builder import BoardControllerBuilder
from chess.field.board_controller import BoardController
from chess.team.team_service import TeamService


class TeamPlacementManager:

    @staticmethod
    def place_teams(board_controller: BoardController):
        for chess_piece in board_controller.team_service.chess_pieces():
            for placement in PlacementChart:
                square_name = placement.map_chess_piece_to_square_name(chess_piece)
                if square_name is not None:
                    square = board_controller.square_service.find_square_by_name(square_name)
                    square.occupy(chess_piece)

