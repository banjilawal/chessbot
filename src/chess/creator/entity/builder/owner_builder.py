import random

from chess.system.identity.id import id_emitter
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.greedy import GreedyEngine
from chess.competitor.commander import CyberneticCommander
from chess.competitor.commander import HumanCommander
from chess.competitor.commander import Commander
from chess.randomize.competitor import RandomName


class OwnerBuilder:

  @staticmethod
  def build(owner_id: int) -> Commander:
    if random.random() < 0.46:
      decision_engine = GreedyEngine(
        engine_id=owner_id,
        board_analyzer=BoardAnalyzer()
      )
      return CyberneticCommander(
        competitor_id=owner_id,
        name=RandomName.cybernaut(),
        decision_engine=decision_engine
      )
    else:
      return HumanCommander(competitor_id=owner_id, name=RandomName.person())


def main():

  owner = OwnerBuilder.build(id_emitter.person_id)
  print(owner, owner.teams.size())

if __name__ == "__main__":
  main()