
from chess.coord import Coord
from chess.piece import Discovery


class DiscoveryDTO:
    _name: str
    _ransom: int
    _piece_id: int
    _rank_name: str
    _team_id: id
    _team_name: str
    _position: Coord

    @classmethod
    def create_from_discovery(cls, discovery: Discovery):
        cls._piece_id = discovery.id
        cls._name = discovery.name
        cls._rank_name = discovery.rank_name
        cls._team_name = discovery.team_name
        cls._position = discovery.position
        return cls

    def to_dict(self):
        return {
            "visitor_name": self._name,
            "visitor_ransom": self._ransom,
            "piece_id": self._piece_id,
            "visitor_rank": self._rank_name,
            "visitor_team_id": self._team_id,
            "visitor_name": self._team_name,
            "position": self._position
        }
