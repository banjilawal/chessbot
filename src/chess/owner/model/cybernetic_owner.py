from typing import Optional, List, Dict


from chess.geometry.coordinate.coordinate import Coordinate

from chess.team.element.piece import ChessPiece
from chess.owner.model.owner import Owner
from chess.team.element.team import Team
from engine.engine import Engine


class CyberneticOwner(Owner):
    _engine: Engine

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None, engine: Engine = None):
        super().__init__(owner_id, name, team)
        self._engine = engine

    @property
    def engine(self) -> Engine:
        return self._engine
