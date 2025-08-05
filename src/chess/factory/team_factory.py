from typing import List

from chess.factory.builder.chess_piece_builder import ChessPieceBuilder
from chess.factory.builder.team_builder import TeamBuilder
from chess.factory.emit import id_emitter
from chess.factory.rank_factory import RankFactory
from chess.team.team import Team
from chess.team.team_config import TeamConfig


class TeamFactory:

    @staticmethod
    def assemble() -> List[Team]:
        teams: List[Team] = []

        for team_config in TeamConfig:
            print(team_config)
            team = TeamBuilder.build(team_config)
            teams.append(team)

        ranks = RankFactory.assemble()
        for rank in ranks:
            print(rank)

        for team in teams:
            for rank in ranks:
                for i in range(rank.number_per_player):
                    chess_piece = ChessPieceBuilder.build(id_emitter.chess_piece_id, (i + 1), rank=rank, team=team)
                    print(chess_piece)
        return teams




def main():
    teams = TeamFactory.assemble()
    for team in teams:
        print(team)

if __name__ == "__main__":
    main()