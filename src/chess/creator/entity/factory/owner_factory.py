from typing import List

from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.creator.entity.factory.rank_factory import RankFactory
from chess.config.team_config import TeamConfig
from chess.owner.human_owner import HumanOwner
from chess.owner.owner import Owner
from chess.randomize.name import RandomName
from chess.team.team import Team


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
        #             chess_piece = ChessPieceBuilder.build(
        #                 token_id=id_emitter.token_id,
        #                 team_rank_member_id=(i + 1),
        #                 rank=rank,
        #                 team=team
        #             )
        #             # print(chess_piece)
        # return teams




def main():
    owners = OwnerFactory.assemble()
    for owner in owners:
        print(owner, ",", len(owner.team.chess_pieces))

    # for team in teams:
    #     for chess_piece in team.chess_pieces:
    #         print(chess_piece)

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