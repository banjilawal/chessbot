from abc import ABC
from typing import Optional, List
from chess.team.team import Team
from chess.team.team_stack import TeamStack


# if TYPE_CHECKING:


class Owner(ABC):
    _id: int
    _name: str
    _team_stack: TeamStack

    def __init__(self, owner_id: int, name: str):
        self._id = owner_id
        self._name = name
        self._team_stack =TeamStack()


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team_stack(self) -> TeamStack:
        return self._team_stack


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
        current_team = self._team_stack.current_team()
        current_team_str = f"current_team:{current_team.id}, {current_team.color}" if (
            current_team) else "current_team:None"
        return (
            f"Player[id:{self._id} "
            f"name:{self._name} {current_team_str} "
            f"teams owned {self._team_stack.size()}]"
        )