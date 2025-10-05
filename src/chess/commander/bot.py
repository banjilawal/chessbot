from abc import ABC
from typing import Optional, cast, TYPE_CHECKING

from chess.coord import CoordValidator
from assurance import IdValidator, NameValidator
from chess.team import Team
from chess.piece import Piece
from chess.commander import CommandHistory

class Bot(Commander):
    _engine: DecisionEngine

    def __init__(self, bot_id: int,name: str,engine: DecisionEngine):
        super().__init__(bot_id, name)
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
        return f"{super().__str__()} engine:{self._engine.__class__.__name__.title()}"