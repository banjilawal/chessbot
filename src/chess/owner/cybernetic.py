from typing import Optional

from chess.owner.base import Owner
from chess.team.model import Team
from chess.engine.decision.decision_engine import DecisionEngine


class CyberneticOwner(Owner):
    _decision_engine: DecisionEngine

    def __init__(
            self,
            owner_id: int,
            name: str,
            decision_engine: DecisionEngine,
    ):
        super().__init__(owner_id, name)
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

    def __str__(self):
        return f"{super().__str__()} engine:{self.decision_engine.__class__.__name__.title()}"
