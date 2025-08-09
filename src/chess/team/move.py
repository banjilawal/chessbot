from chess.geometry.coordinate.coordinate import Coordinate
from chess.token.piece import ChessPiece
from chess.team.element.team import Team


class Move:
    _team: Team
    _team_member: ChessPiece
    _destination: Coordinate

    def __init__(self, team: Team, team_member: ChessPiece, destination: Coordinate):
        self._team = team
        self._team_member = team_member
        self._destination = destination

    @property
    def team(self) -> Team:
        return self._team

    @property
    def team_member(self) -> ChessPiece:
        return self._team_member

    @property
    def destination(self) -> Coordinate:
        return self._destination