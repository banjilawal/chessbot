from chess.rank.bishop import Bishop
from chess.rank.rook import Rook
from chess.rank.king import King
from chess.rank.knight import Knight
from chess.pawn import Pawn
from chess.rank.spec import RankSpec
from chess.rank.queen import Queen


class RankBuilder:

  @staticmethod
  def build(config: RankSpec):

    if config is RankSpec.KING:
      return King(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is RankSpec.PAWN:
      return Pawn(
        name=config.name,
        letter=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is RankSpec.KNIGHT:
      return Knight(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is RankSpec.BISHOP:
      return Bishop(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is RankSpec.ROOK:
      return Rook(
        name=config.name,
        designation=config.designation,
        team_quota=config.number_per_team,
        quadrants=config.quadrants,
        ransom=config.capture_value
      )
    if config is RankSpec.QUEEN:
      return Queen(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    raise ValueError(f"Invalid rank config: {config}")



def main():
  rank = RankBuilder.build(RankSpec.PAWN)
  print(rank)


if __name__ == "__main__":
  main()