import random

from chess.common.emit import id_emitter
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.greedy_decision_engine import GreedyDecisionEngine
from chess.competitor.commander import CyberneticCommander
from chess.competitor.commander import HumanCommander
from chess.competitor.commander import Commander
from chess.randomize.competitor import RandomName


class OwnerBuilder:

    @staticmethod
    def build(owner_id: int) -> Commander:
        if random.random() < 0.46:
            decision_engine = GreedyDecisionEngine(
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
    print(owner, owner.teams_played.size())

if __name__ == "__main__":
    main()