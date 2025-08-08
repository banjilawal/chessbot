from chess.creator.service.square_service_builder import SquareServiceBuilder
from chess.creator.service.team_service_builder import TeamServiceBuilder

from chess.field.board_controller import BoardController


class BoardControllerBuilder:

    @staticmethod
    def build() -> BoardController:

        team_service = TeamServiceBuilder.assemble()
        square_service = SquareServiceBuilder.assemble()

        board_controller = BoardController(team_service=team_service, square_service=square_service)

        from chess.creator.team_placement_manager import TeamPlacementManager
        TeamPlacementManager.place_teams(board_controller)
        return board_controller
        # BoardControllerBuilder.place_teams(team_service, square_service)
        # return ArenaController(team_service=team_service, square_service=square_service)
        # teams: List[Team] = []
        #
        # for team_config in TeamConfig:
        #     print(team_config)
        #     team = TeamBuilder.build(team_config)
        #     teams.append(team)
        #
        # motion_controllers = RankFactory.assemble()
        # for rank in motion_controllers:
        #     print(rank)
        #
        # for team in teams:
        #     for rank in motion_controllers:
        #         for i in range(rank.number_per_team):
        #             chess_piece = ChessPieceBuilder.build(
        #                 id_emitter.chess_piece_id,
        #                 (i + 1),
        #                 rank=rank,
        #                 team=team
        #             )
        #             # print(chess_piece)
        # return teams
    #
    # @staticmethod
    # def place_teams(team_service: TeamService, square_service: MapService):
    #
    #     for chess_piece in team_service.chess_pieces():
    #         for placement in PlacementChart:
    #             square_name = placement.map_chess_piece_to_square_name(chess_piece)
    #             if square_name is not None:
    #                 map = square_service.find_square_by_name(square_name)
    #                 map.occupy(chess_piece)
    #                 print(map)

#
#
#
#
#
# def main():
#     square_service = SquareServiceBuilder.assemble()
#     team_service = TeamServiceBuilder.assemble()
#     board_controller = BoardControllerBuilder.build(team_service, square_service)
#
#     print(board_controller.square_service.squares_to_string())
#
#
# if __name__ == "__main__":
#     main()