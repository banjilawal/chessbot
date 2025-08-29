from typing import List

from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.config.team import TeamConfig
from chess.owner.human import HumanOwner
from chess.owner.base import Owner
from chess.randomize.name import RandomName
from chess.team.model import Team


class OwnerFactory:

    @staticmethod
    def assemble() -> List[Owner]:
        owners: List[Owner] = []

        wo = HumanOwner(owner_id=id_emitter.owner_id, name=RandomName.person_name())
        bo = HumanOwner(owner_id=id_emitter.owner_id, name=RandomName.person_name())

        wt = TeamBuilder.build(wo, TeamConfig.WHITE)
        bt = TeamBuilder.build(bo, TeamConfig.BLACK)

        ranks = RankFactory.assemble()
        for team in [wt, bt]:
            for rank in ranks:
                for i in range(rank.number_per_team):
                    chess_piece = ChessPieceBuilder.build(
                        token_id=id_emitter.token_id,
                        team_rank_member_id=(i + 1),
                        rank=rank,
                        team=team
                    )
        owners.append(wo)
        owners.append(bo)
        return owners
        #
        #
        #
        # for team_config in TeamConfig:
        #     # print(team_config)
        #     team = TeamBuilder.build(OwnerBuilder.build(id_emitter.owner_id), team_config)
        #     teams.append(team)
        #
        #
        # # for rank in ranks:
        # #     print(rank)
        #
        # for team in teams:
        #     for rank in ranks:
        #         for i in range(rank.number_per_team):
        #             captor = ChessPieceBuilder.build(
        #                 token_id=id_emitter.token_id,
        #                 team_rank_member_id=(i + 1),
        #                 rank=rank,
        #                 team=team
        #             )
        #             # print(captor)
        # return teams




def main():
    owners = OwnerFactory.assemble()
    for owner in owners:
        print(owner, ",", len(owner.team.pieces))

    # for team in teams:
    #     for captor in team.chess_pieces:
    #         print(captor)

            # for placement in PlacementChart:
            #     square_name = placement.map_chess_piece_to_square_name(captor)
            #     if square_name is not None:
            #         chessboard = chess_board.find_square_by_name(square_name)
            #         chessboard(captor)
            #         print(chessboard)
    # print(repo)
                    # print(chessboard.name, " occupied by", chessboard.occupant.name)
                # print(placement.value[0])
                # placement.map_chess_piece_to_square_name(captor)
                # print("comparing", placement.chess_piece_name.capitalize(), " with", captor.name.capitalize())
                # captor.name.capitalize() == placement.value[0].capitalize():

       # print(f"matched chessboard:{placement.square_name} with {captor.name}")`````````

if __name__ == "__main__":
    main()