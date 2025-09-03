import random

from chess.config.owner import OwnerConfig
from chess.creator.emit import id_emitter
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.greedy_decision_engine import GreedyDecisionEngine
from chess.competitor.model import CyberneticCompetitor
from chess.competitor.model import HumanCompetitor
from chess.competitor.model import Competitor
from chess.randomize.name import RandomName


class OwnerBuilder:

    @staticmethod
    def build(owner_id: int) -> Competitor:
        if random.random() < 0.46:
            decision_engine = GreedyDecisionEngine(
                engine_id=owner_id,
                board_analyzer=BoardAnalyzer()
            )
            return CyberneticCompetitor(
                competitor_id=owner_id,
                name=RandomName.cybernaut_name(),
                decision_engine=decision_engine
            )
        else:
            return HumanCompetitor(competitor_id=owner_id, name=RandomName.person_name())


def main():

    owner = OwnerBuilder.build(id_emitter.owner_id)
    print(owner, owner.sides_played.size())

if __name__ == "__main__":
    main()