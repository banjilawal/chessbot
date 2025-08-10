from typing import List

from chess.config.placement_chart import PlacementChart
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.config.team_config import TeamConfig
from chess.creator.service.chess_board_builder import ChessBoardBuilder
from chess.owner.owner import Owner
from chess.team.team import Team


class TeamFactory:

    @staticmethod
    def assemble() -> List[Team]:
        teams: List[Team] = []

        for team_config in TeamConfig:
            print(team_config)
            team = TeamBuilder.build(OwnerBuilder.build(id_emitter.owner_id), team_config)
            teams.append(team)

        ranks = RankFactory.assemble()
        for rank in ranks:
            print(rank)

        for team in teams:
            for rank in ranks:
                for i in range(rank.number_per_team):
                    chess_piece = ChessPieceBuilder.build(
                        id_emitter.token_id,
                        (i + 1),
                        rank=rank,
                        team=team
                    )
                    print(chess_piece)
        return teams




def main():
    teams = TeamFactory.assemble()
    for team in teams:
        print(team)

    chess_board = ChessBoardBuilder.build()

    for team in teams:
        for chess_piece in team.chess_pieces:
            print(chess_piece)

            # for placement in PlacementChart:
            #     square_name = placement.map_chess_piece_to_square_name(chess_piece)
            #     if square_name is not None:
            #         board = chess_board.find_square_by_name(square_name)
            #         board(chess_piece)
            #         print(board)
    # print(repo)
                    # print(board.name, " occupied by", board.occupant.name)
                # print(placement.value[0])
                # placement.map_chess_piece_to_square_name(chess_piece)
                # print("comparing", placement.chess_piece_name.capitalize(), " with", chess_piece.name.capitalize())
                # chess_piece.name.capitalize() == placement.value[0].capitalize():

       # print(f"matched board:{placement.square_name} with {chess_piece.name}")`````````

if __name__ == "__main__":
    main()