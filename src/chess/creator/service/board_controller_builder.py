from typing import List


from chess.config.placement_chart import PlacementChart
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.motion_controller_factory import MotionControllerFactory
from chess.creator.service.square_service_builder import SquareServiceBuilder
from chess.creator.service.team_service_builder import TeamServiceBuilder
from chess.field.board_controller import BoardController
from chess.square import repo
from chess.config.team_config import TeamConfig
from chess.square.service.square_service import SquareService
from chess.team.model.team import Team
from chess.team.team_service import TeamService


class BoardControllerBuilder:

    @staticmethod
    def build(team_service: TeamService, square_service: SquareService) -> BoardController:

        BoardControllerBuilder.place_teams(team_service, square_service)
        return BoardController(team_service=team_service, square_service=square_service)
        # teams: List[Team] = []
        #
        # for team_config in TeamConfig:
        #     print(team_config)
        #     team = TeamBuilder.build(team_config)
        #     teams.append(team)
        #
        # motion_controllers = MotionControllerFactory.assemble()
        # for motion_controller in motion_controllers:
        #     print(motion_controller)
        #
        # for team in teams:
        #     for motion_controller in motion_controllers:
        #         for i in range(motion_controller.number_per_player):
        #             chess_piece = ChessPieceBuilder.build(
        #                 id_emitter.chess_piece_id,
        #                 (i + 1),
        #                 motion_controller=motion_controller,
        #                 team=team
        #             )
        #             # print(chess_piece)
        # return teams

    @staticmethod
    def place_teams(team_service: TeamService, square_service: SquareService):

        for chess_piece in team_service.chess_pieces():
            for placement in PlacementChart:
                square_name = placement.map_chess_piece_to_square_name(chess_piece)
                if square_name is not None:
                    square = square_service.find_square_by_name(square_name)
                    square.occupy(chess_piece)
                    print(square)






def main():
    square_service = SquareServiceBuilder.assemble()
    team_service = TeamServiceBuilder.assemble()
    board_controller = BoardControllerBuilder.build(team_service, square_service)

    print(board_controller.square_service.squares_to_string())


if __name__ == "__main__":
    main()