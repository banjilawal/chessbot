from typing import List


from chess.config.placement_chart import PlacementChart
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.motion_controller_factory import MotionControllerFactory
from chess.creator.service.square_service_builder import SquareServiceBuilder
from chess.map import repo
from chess.config.team_config import TeamConfig
from chess.map.service.grid_service import GridService
from chess.team.model.team import Team


class TeamFactory:

    @staticmethod
    def assemble() -> List[Team]:
        teams: List[Team] = []

        for team_config in TeamConfig:
            print(team_config)
            team = TeamBuilder.build(team_config)
            teams.append(team)

        motion_controllers = MotionControllerFactory.assemble()
        for motion_controller in motion_controllers:
            print(motion_controller)

        for team in teams:
            for motion_controller in motion_controllers:
                for i in range(motion_controller.number_per_team):
                    chess_piece = ChessPieceBuilder.build(
                        id_emitter.chess_piece_id,
                        (i + 1),
                        motion_controller=motion_controller,
                        team=team
                    )
                    # print(chess_piece)
        return teams



#
# def main():
#     teams = TeamFactory.assemble()
#     for team in teams:
#         print(team)
#
#     square_service = SquareServiceBuilder.assemble()
#
#     for team in teams:
#         for chess_piece in team.chess_pieces:
#
#             for placement in PlacementChart:
#                 square_name = placement.map_chess_piece_to_square_name(chess_piece)
#                 if square_name is not None:
#                     map = square_service.find_square_by_name(square_name)
#                     map.occupy(chess_piece)
#                     print(map)
#     print(repo)
#                     # print(map.name, " occupied by", map.occupant.name)
#                 # print(placement.value[0])
#                 # placement.map_chess_piece_to_square_name(chess_piece)
#                 # print("comparing", placement.chess_piece_name.capitalize(), " with", chess_piece.name.capitalize())
#                 # chess_piece.name.capitalize() == placement.value[0].capitalize():
#
#        # print(f"matched map:{placement.square_name} with {chess_piece.name}")`````````
#
# if __name__ == "__main__":
#     main()