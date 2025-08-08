from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.geometry.coordinate.coordinate import Coordinate
from chess.team.element.piece import ChessPiece


class Move:
    _team: TeamBuilder
    _team_member: ChessPiece
    _destination: Coordinate

    def __init__(self, team: TeamBuilder, team_member: ChessPiece, destination: Coordinate):
        self._team = team
        self._team_member = team_member
        self._destination = destination

    @property
    def team(self) -> TeamBuilder:
        return self._team

    @property
    def team_member(self) -> ChessPiece:
        return self._team_member

    @property
    def destination(self) -> Coordinate:
        return self._destination