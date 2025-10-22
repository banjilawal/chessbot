from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from typing import Optional


from chess.team import Team
from chess.system import DTO


class TeamDTO(DTO[Team]):
    _id: int
    _name: str
    _commander_id: int
    _commander_name: str
    
    def __init__(
            self,
            id: int,
            name: str,
            commander_id: int,
            commander_name: str
    ):
        self._id = id
        self._name = name
        self._commander_id = commander_id
        self._commander_name = commander_name
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def commander_id(self) -> int:
        self._commander_id
        
    @property
    def commander_name(self) -> str:
        self._commander_name

    
    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "commander_id": self._commander_id,
            "captor_name": self._commander_name
        }



