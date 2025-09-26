from typing import List

from chess.common.emitter import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.team.team_profile import TeamProfile
from chess.competitor.commander import HumanCommander
from chess.competitor.commander import Commander
from chess.randomize.competitor import RandomName


class OwnerFactory:

    @staticmethod
    def assemble() -> List[Commander]:
        owners: List[Commander] = []

        wo = HumanCommander(competitor_id=id_emitter.person_id, name=RandomName.person())
        bo = HumanCommander(competitor_id=id_emitter.person_id, name=RandomName.person())

        wt = TeamBuilder.build(wo, TeamProfile.WHITE)
        bt = TeamBuilder.build(bo, TeamProfile.BLACK)

        ranks = RankFactory.assemble()
        for team in [wt, bt]:
            for rank in ranks:
                for i in range(rank.per_side):
                    chess_piece = ChessPieceBuilder.build(
                        token_id=id_emitter.id,
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
        #     team = TeamBuilder.build(OwnerBuilder.build(id_emitter.commander_id), team_config)
        #     teams.append(team)
        #
        #
        # # for validation in ranks:
        # #     print(validation)
        #
        # for team in teams:
        #     for validation in ranks:
        #         for i in range(validation.number_per_team):
        #             captor = ChessPieceBuilder.build(
        #                 piece_id=id_emitter.piece_id,
        #                 team_rank_member_id=(i + 1),
        #                 validation=validation,
        #                 team=team
        #             )
        #             # print(captor)
        # return teams




def main():
    owners = OwnerFactory.assemble()
    for owner in owners:
        print(owner, ",", len(owner.team.roster))

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