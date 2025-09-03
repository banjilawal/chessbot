
from chess.config.team import SideProfile
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.chess_piece_builder import ChessPieceBuilder
from chess.creator.entity.builder.owner_builder import OwnerBuilder
from chess.competitor.model import Competitor
from chess.team.model import Side


class TeamBuilder:

    @staticmethod
    def build(owner: Competitor, config: SideProfile) -> Side:
       print("build team got config", config)
       team = Side(
           team_id=id_emitter.team_id,
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
#         competitor = OwnerBuilder.build(id_emitter.owner_id)
#         team = TeamBuilder.build(competitor, config)
#         print(team)
#         if team not in teams:
#             teams.append(team)
#     print(len(teams))
#
#     old_owwer = teams[0].competitor
#     teams[0].competitor = None
#     print(teams[0])
#
#     teams[0].competitor = OwnerBuilder.build(id_emitter.owner_id)
#     print(teams[0])
#
#     team = TeamBuilder.build(old_owwer, TeamConfig.WHITE)
#     print(team)
#     print(old_owwer)
#
#
# if __name__ == "__main__":
#     main()