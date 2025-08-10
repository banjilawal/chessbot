import random

from chess.config.owner_config import OwnerConfig
from chess.creator.emit import id_emitter
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.greedy_decision_engine import GreedyDecisionEngine
from chess.owner.cybernetic_owner import CyberneticOwner
from chess.owner.human_owner import HumanOwner
from chess.owner.owner import Owner
from chess.randomize.name import RandomName


class OwnerBuilder:

    @staticmethod
    def build(owner_id: int) -> Owner:
        if random.random() < 0.46:
            decision_engine = GreedyDecisionEngine(
                engine_id=owner_id,
                board_analyzer=BoardAnalyzer()
            )
            return CyberneticOwner(
                owner_id=owner_id,
                name=RandomName.cybernaut_name(),
                decision_engine=decision_engine
            )
        else:
            return HumanOwner(owner_id=owner_id, name=RandomName.person_name())


def main():

    owner = OwnerBuilder.build(id_emitter.owner_id)
    print(owner, owner.team_stack.size())

if __name__ == "__main__":
    main()