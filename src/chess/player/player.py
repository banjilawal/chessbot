from abc import abstractmethod, ABC

from chess.common.piece import Piece
from chess.team.team import Team


class Player(ABC):
    _id: int
    _name: str
    _team: Team
    def __init__(self, player_id: int, name: str, team: Team):
        self._id = player_id
        self._name = name
        self._team  team

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def team(self) -> Team:
        return self._team