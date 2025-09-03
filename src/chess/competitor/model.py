from abc import ABC
from typing import Optional, cast, TYPE_CHECKING

from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from chess.engine.decision.decision_engine import DecisionEngine

from chess.competitor.side import SideRecord

if TYPE_CHECKING:
    from chess.team.model import Side


class Competitor(ABC):
    _id: int
    _name: str
    _current_side: Optional['Side']
    _sides_played: SideRecord

    def __init__(self, competitor_id: int, name: str):

        id_validation = IdValidator.validate(competitor_id)
        if not id_validation.is_success():
            raise id_validation.exception

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise name_validation.exception

        self._id = cast(id_validation.payload.id, int)
        self._name = cast(name_validation.payload.name, str)
        self._sides_played = SideRecord()

        self._current_side = self._sides_played.current_side


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def sides_played(self) -> SideRecord:
        return self._sides_played


    @property
    def current_side(self) -> Optional['Side']:
        return self._sides_played.current_side


    @name.setter
    def name(self, name: str):
        self._name = name


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Competitor):
            return False
        return self.id == other.id


    def __str__(self):
        total_games = self.sides_played.size()
        total_games_str = f"total games:{total_games}" if total_games > 0 else ""

        current_side = "" if self._current_side is None else \
            f" curren_team:[{self._current_side.id}, {self._current_side.profile.color}"
        return (
            f"Owner[id:{self._id}"
            f" name:{self._name}"
            f"{current_side}"
            f"{total_games_str}"
            f"]"
        )


class HumanCompetitor(Competitor):

    def __init__(self, competitor_id: int, name: str):
        super().__init__(competitor_id, name)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, HumanCompetitor):
            return self.id == other.id
        return False


class CyberneticCompetitor(Competitor):
    _decision_engine: DecisionEngine

    def __init__(
            self,
            competitor_id: int,
            name: str,
            decision_engine: DecisionEngine,
    ):
        super().__init__(competitor_id, name)
        self._decision_engine = decision_engine


    @property
    def decision_engine(self) -> DecisionEngine:
        return self._decision_engine


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, CyberneticCompetitor):
            return self._id == other.id
        return False

    def __str__(self):
        return f"{super().__str__()} engine:{self.decision_engine.__class__.__name__.title()}"