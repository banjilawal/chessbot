from chess.rank.model.concrete.bishop import Bishop
from chess.rank.model.concrete.rook import Rook
from chess.rank.model.concrete.king import King
from chess.rank.model.concrete.knight import Knight
from chess.pawn import Pawn
from chess.rank.spec import RankSpec
from chess.rank.model.concrete.queen import Queen


class RankBuilder:

  @staticmethod
  def build(config: RankSpec):

    if config is Persona.KING:
      return King(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is Persona.PAWN:
      return Pawn(
        name=config.name,
        letter=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is Persona.KNIGHT:
      return Knight(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is Persona.BISHOP:
      return Bishop(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    if config is Persona.ROOK:
      return Rook(
        name=config.name,
        designation=config.designation,
        team_quota=config.number_per_team,
        quadrants=config.quadrants,
        ransom=config.capture_value
      )
    if config is Persona.QUEEN:
      return Queen(
        name=config.name,
        designation=config.designation,
        per_side=config.number_per_team,
        quadrants=config.quadrants,
        value=config.capture_value
      )
    raise ValueError(f"Invalid rank config: {config}")



def main():
  rank = RankBuilder.build(Persona.PAWN)
  print(rank)


if __name__ == "__main__":
  main()