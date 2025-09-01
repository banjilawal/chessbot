from abc import ABC
from typing import Optional, cast

from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from chess.team.model import Team
from chess.team.stack import TeamHistory


class Owner(ABC):
    _id: int
    _name: str
    _current_team: Optional[Team]
    _team_history: TeamHistory

    def __init__(self, owner_id: int, name: str):

        id_validation = IdValidator.validate(owner_id)
        if not id_validation.is_success():
            raise id_validation.exception

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise name_validation.exception

        self._id = cast(id_validation.payload.id, int)
        self._name = cast(name_validation.payload.name, str)
        self._team_history =TeamHistory()

        self._current_team = self._team_history.current_team


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team_history(self) -> TeamHistory:
        return self._team_history


    @property
    def current_team(self) -> Optional[Team]:
        return self._team_history.current_team


    @name.setter
    def name(self, name: str):
        self._name = name


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Owner):
            return False
        return self.id == other.id


    def __str__(self):
        history_size = self.team_history.size()
        team_size_str = f"total games:{history_size}" if history_size > 0 else ""

        current_team_str = "" if self._current_team is None else \
            f" curren_team:[{self._current_team.id}, {self._current_team.color}"
        return (
            f"Owner[id:{self._id}"
            f" name:{self._name}"
            f"{current_team_str}"
            f"{team_size_str }"
            f"]"
        )