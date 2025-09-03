from chess.geometry.coord import Coordinate
from chess.team.model import Side
from chess.token.model.base import Piece


class Move:
    _team: Side
    _destination: Coordinate

    def __init__(self, team: Side, team_member: Piece, destination: Coordinate):
        self._team = team
        self._team_member = team_member
        self._destination = destination


    @property
    def team(self) -> Side:
        return self._team


    @property
    def team_member(self) -> Piece:
        return self._team_member


    @property
    def destination(self) -> Coordinate:
        return self._destination