from chess.config.owner_config import OwnerConfig
from chess.creator.emit import id_emitter
from chess.engine.analyze.board_analyzer import BoardAnalyzer
from chess.engine.decision.greedy_decision_engine import GreedyDecisionEngine
from chess.owner.cybernetic_owner import CyberneticOwner
from chess.owner.human_owner import HumanOwner
from chess.owner.owner import Owner


class OwnerBuilder:

    @staticmethod
    def build(owner_id: int, name: str, owner_config: OwnerConfig) -> Owner:
        if owner_config is OwnerConfig.CYBERNETIC:
            decision_engine = GreedyDecisionEngine(
                engine_id=id_emitter.engine_id,
                board_analyzer=BoardAnalyzer()
            )
            return CyberneticOwner(owner_id=owner_id, name=name, decision_engine=decision_engine)

        return HumanOwner(owner_id=owner_id, name=name)


def main():

    owner = OwnerBuilder.build(
        owner_id=id_emitter.owner_id1,
        name="banji", OwnerConfig.CYBERNETIC
    )

    print(owner)

if __name__ == "__main__":
    main()