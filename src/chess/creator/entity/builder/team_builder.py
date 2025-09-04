
from chess.config.game import SideProfile
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.competitor.model import Competitor
from chess.side.model import Side


class TeamBuilder:

    @staticmethod
    def build(owner: Competitor, config: SideProfile) -> Side:
       print("build side got config", config)
       team = Side(
           side_id=id_emitter.side_id,
           letter=config.letter,
           team_color=config.game_color,
           back_row_index=config.back_rank_index,
           pawn_row_index=config.pawn_rank_index,
           home_quadrant=config.quadrant,
           controller=owner
       )
       return team



#
# def main():
#     teams: list[Team] = []
#     for config in TeamConfig:
#         competitor = OwnerBuilder.build(id_emitter.competitor_id)
#         side = TeamBuilder.build(competitor, config)
#         print(side)
#         if side not in teams:
#             teams.append(side)
#     print(len(teams))
#
#     old_owwer = teams[0].competitor
#     teams[0].competitor = None
#     print(teams[0])
#
#     teams[0].competitor = OwnerBuilder.build(id_emitter.competitor_id)
#     print(teams[0])
#
#     side = TeamBuilder.build(old_owwer, TeamConfig.WHITE)
#     print(side)
#     print(old_owwer)
#
#
# if __name__ == "__main__":
#     main()