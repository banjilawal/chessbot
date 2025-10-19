
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
            "name": self._name,
            "ransom": self._ransom,
            "piece_id": self._piece_id,
            "rank_name": self._rank_name,
            "team_id": self._team_id,
            "team_name": self._team_name,
            "position": self._position
        }
