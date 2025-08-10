from abc import ABC
from typing import Optional, List
from chess.team.team import Team

# if TYPE_CHECKING:


class Owner(ABC):
    _id: int
    _name: str
    _teams: List[Team]

    def __init__(self, owner_id: int, name: str):
        self._id = owner_id
        self._name = name
        self._team = []


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def teams(self) -> List[Team]:
        return self._teams


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
        return f"Player[id:{self._id} name:{self._name} team:{self._team}]"