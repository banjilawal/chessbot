from chess.geometry.coord import Coord
from chess.side.team import Side
from chess.piece.piece import Piece


class Move:
    _team: Side
    _destination: Coord

    def __init__(self, team: Side, team_member: Piece, destination: Coord):
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
    def destination(self) -> Coord:
        return self._destination