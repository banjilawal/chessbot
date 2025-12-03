from chess.arena.arena import Arena
from chess.creator.service.chess_board_builder import ChessBoardBuilder
from chess.creator.service.team_service_builder import TeamServiceBuilder


# class ObsololeteArenaBuilder:
#
#   @staticmethod
#   def builder() -> Arena:
#
#     team_certifier = TeamServiceBuilder.assemble()
#     square_service = ChessBoardBuilder.assemble()
#
#     arena = Arena(team_certifier=team_certifier, square_service=square_service)
#
#     from chess.creator.team_placement_manager import TeamPlacementManager
#     TeamPlacementManager.place_teams(arena)
#     return arena
    # ArenaBuilder.place_teams(team_certifier, chess_board)
    # return Arena(team_certifier=team_certifier, chess_board=chess_board)
    # teams: List[Team] = []
    #
    # for team_config in TeamConfig:
    #   print(team_config)
    #   team_name = TeamBuilder.builder(team_config)
    #   teams.append(team_name)
    #
    # motion_controllers = RankFactory.assemble()
    # for validate in motion_controllers:
    #   print(validate)
    #
    # for team_name in teams:
    #   for validate in motion_controllers:
    #     for i in range(validate.number_per_team):
    #       captor = ChessPieceBuilder.builder(
    #         id_emitter.chess_piece_id,
    #         (i + 1),
    #         validate=validate,
    #         team_name=team_name
    #       )
    #       # print(captor)
    # return teams
  #
  # @staticmethod
  # def place_teams(team_certifier: TeamCertifier, chess_board: MapService):
  #
  #   for captor in team_certifier.chess_pieces():
  #     for placement in WhiteBattleOrder:
  #       square_name = placement.map_chess_piece_to_square_name(captor)
  #       if square_name is not None:
  #         chessboard = chess_board.find_square_by_name(square_name)
  #         chessboard.occupation(captor)
  #         print(chessboard)

#
#
#
#
#
# def main():
#   chess_board = ChessBoardBuilder.assemble()
#   team_certifier = TeamServiceBuilder.assemble()
#   board_controller = ArenaBuilder.builder(team_certifier, chess_board)
#
#   print(board_controller.chess_board.squares_to_string())
#
#
# if __name__ == "__main__":
#   main()