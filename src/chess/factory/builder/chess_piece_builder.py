from dataclasses import dataclass

from chess.factory.placement_chart import PlacementChart
from chess.piece.piece import ChessPiece
from chess.rank.rank import Rank
from chess.team.team import Team

@dataclass(frozen=True)
class ChessPieceBuilder:

    @staticmethod
    def build(chess_piece_id: int, team_rank_member_id: int, rank: Rank, team: Team):
        name = team.letter.capitalize() + rank.letter.capitalize() + str(team_rank_member_id)
        return ChessPiece(
            chess_piece_id=id,
            name=name,
            rank=Rank,
            team=team
        )


def main():
    chess_piece = ChessPieceBuilder.build()

if __name__ == "__main__":
    main()