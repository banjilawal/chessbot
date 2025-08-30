from typing import Optional

from chess.rank.base import Rank
from chess.team.model import Team
from chess.token.model.base import Piece


class Combatant(Piece):
    _captor: Optional[Piece]

    def __init__(self, token_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(token_id, name, rank, team)
        self._captor = None


    @property
    def captor(self) -> Optional[Piece]:
        return self._captor


    @captor.setter
    def captor(self, captor: Piece):
        self._captor = captor


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, Combatant):
            return self.id == other.id