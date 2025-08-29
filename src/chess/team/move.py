from chess.geometry.coordinate.coord import Coordinate
from chess.token.model import Piece
from chess.team.model import Team


class Move:
    _team: Team
    _destination: Coordinate

    def __init__(self, team: Team, team_member: Piece, destination: Coordinate):
        self._team = team
        self._team_member = team_member
        self._destination = destination

    @property
    def team(self) -> Team:
        return self._team

    @property
    def team_member(self) -> Piece:
        return self._team_member

    @property
    def destination(self) -> Coordinate:
        return self._destination