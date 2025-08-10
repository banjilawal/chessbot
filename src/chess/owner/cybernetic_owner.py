from typing import Optional

from chess.owner.owner import Owner
from chess.team.team import Team
from chess.engine.decision.decision_engine import DecisionEngine


class CyberneticOwner(Owner):
    _decision_engine: DecisionEngine

    def __init__(
            self, owner_id: int,
            name: str,
            decision_engine: DecisionEngine,
            team: Optional[Team] = None
    ):
        super().__init__(owner_id, name, team)
        self._decision_engine = decision_engine


    @property
    def decision_engine(self) -> DecisionEngine:
        return self._decision_engine


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, CyberneticOwner):
            return self._id == other.id
        return False
