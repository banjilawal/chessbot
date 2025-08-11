from typing import List

from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.config.team_config import TeamConfig
from chess.team.team import Team


class TeamFactory:

    @staticmethod
    def assemble() -> List[Team]:
        teams: List[Team] = []

        for team_config in TeamConfig:
            # print(team_config)
            team = TeamBuilder.build(OwnerBuilder.build(id_emitter.owner_id), team_config)
            teams.append(team)

        ranks = RankFactory.assemble()
        # for rank in ranks:
        #     print(rank)

        for team in teams:
            for rank in ranks:
                for i in range(rank.number_per_team):
                    chess_piece = ChessPieceBuilder.build(
                        token_id=id_emitter.token_id,
                        team_rank_member_id=(i + 1),
                        rank=rank,
                        team=team
                    )
                    # print(captor)
        return teams




def main():
    teams = TeamFactory.assemble()
    for team in teams:
        print(team)

    # for team in teams:
    #     for captor in team.chess_pieces:
    #         print(captor)

            # for placement in PlacementChart:
            #     square_name = placement.map_chess_piece_to_square_name(captor)
            #     if square_name is not None:
            #         board = chess_board.find_square_by_name(square_name)
            #         board(captor)
            #         print(board)
    # print(repo)
                    # print(board.name, " occupied by", board.occupant.name)
                # print(placement.value[0])
                # placement.map_chess_piece_to_square_name(captor)
                # print("comparing", placement.chess_piece_name.capitalize(), " with", captor.name.capitalize())
                # captor.name.capitalize() == placement.value[0].capitalize():

       # print(f"matched board:{placement.square_name} with {captor.name}")`````````

if __name__ == "__main__":
    main()