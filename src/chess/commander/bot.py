from chess.commander import Commander
from chess.engine import DecisionEngine


class Bot(Commander):
    _engine: DecisionEngine

    def __init__(
            self,
            commander_id: int,
            name: str,
            engine: DecisionEngine,
    ):
        super().__init__(commander_id, name)
        self._engine = engine


    @property
    def engine(self) -> DecisionEngine:
        return self._engine


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, Bot):
            return self._id == other.id
        return False

    def __str__(self):
        return f"{super().__str__()} engine:{self.decision_engine.__class__.__name__.title()}"