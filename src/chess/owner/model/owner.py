from abc import ABC
from typing import List, TYPE_CHECKING, Optional
from chess.team.element.team import Team

# if TYPE_CHECKING:


class Owner(ABC):
    _id: int
    _name: str
    _team: Team

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        self._id = owner_id
        self._name = name
        self._team = team


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team(self) -> Team:
        return self._team


    @name.setter
    def name(self, name: str):
        self._name = name


    @team.setter
    def team(self, team: Team):
        self._team = team

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Owner):
            return False
        return self.id == other.id





    def __str__(self):
        return f"Player[{self._id} {self._name} {self._team}]"