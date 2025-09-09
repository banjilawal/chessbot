from chess.rank.bishop_rank import Bishop
from chess.rank.rook_rank import Rook
from chess.rank.king_rank import King
from chess.rank.knight_rank import Knight
from chess.rank.pawn_rank import Pawn
from chess.config.rank import RankProfile
from chess.rank.queen_rank import Queen


class RankBuilder:

    @staticmethod
    def build(config: RankProfile):

        if config is RankProfile.KING:
            return King(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        if config is RankProfile.PAWN:
            return Pawn(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        if config is RankProfile.KNIGHT:
            return Knight(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        if config is RankProfile.BISHOP:
            return Bishop(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        if config is RankProfile.CASTLE:
            return Rook(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        if config is RankProfile.QUEEN:
            return Queen(
                name=config.name,
                letter=config.letter,
                per_side=config.number_per_team,
                quadrants=config.quadrants,
                value=config.capture_value
            )
        raise ValueError(f"Invalid rank config: {config}")



def main():
    rank = RankBuilder.build(RankProfile.PAWN)
    print(rank)


if __name__ == "__main__":
    main()