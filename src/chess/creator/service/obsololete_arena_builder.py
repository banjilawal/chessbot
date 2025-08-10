from chess.arena.arena import Arena
from chess.creator.service.chess_board_builder import ChessBoardBuilder
from chess.creator.service.team_service_builder import TeamServiceBuilder


# class ObsololeteArenaBuilder:
#
#     @staticmethod
#     def build() -> Arena:
#
#         team_service = TeamServiceBuilder.assemble()
#         square_service = ChessBoardBuilder.assemble()
#
#         arena = Arena(team_service=team_service, square_service=square_service)
#
#         from chess.creator.team_placement_manager import TeamPlacementManager
#         TeamPlacementManager.place_teams(arena)
#         return arena
        # ArenaBuilder.place_teams(team_service, chess_board)
        # return Arena(team_service=team_service, chess_board=chess_board)
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
    # def place_teams(team_service: TeamService, chess_board: MapService):
    #
    #     for chess_piece in team_service.chess_pieces():
    #         for placement in PlacementChart:
    #             square_name = placement.map_chess_piece_to_square_name(chess_piece)
    #             if square_name is not None:
    #                 board = chess_board.find_square_by_name(square_name)
    #                 board.occupy(chess_piece)
    #                 print(board)

#
#
#
#
#
# def main():
#     chess_board = ChessBoardBuilder.assemble()
#     team_service = TeamServiceBuilder.assemble()
#     board_controller = ArenaBuilder.build(team_service, chess_board)
#
#     print(board_controller.chess_board.squares_to_string())
#
#
# if __name__ == "__main__":
#     main()