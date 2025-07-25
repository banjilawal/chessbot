from abc import abstractmethod, ABC

from chess.common.constant import GameColor
from chess.common.piece import Piece
from chess.team.team import Team


class Player(ABC):
    _id: int
    _name: str
    _team: Team
    _color: GameColor
    def __init__(self, player_id: int, name: str, team: Team, color: GameColor):
        self._id = player_id
        self._name = name
        self._team = team
        self._color = color

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def team(self) -> Team:
        return self._team

    @property
    def color(self) -> GameColor:
        return self._color