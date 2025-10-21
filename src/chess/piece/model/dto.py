

from typing import Optional

from chess.coord import Coord
from chess.piece import Piece, DiscoveryDTO
from chess.piece.model.piece import CombatantPiece


class PieceDTO:
  _id: int
  _name: str
  _ransom: int
  _team_id: int
  _team_name: str
  _rank_name: str
  _current_position: Coord
  _captor_id: Optional[int]
  _captor_name: Optional[str]
  _discoveries: list[DiscoveryDTO]

  @classmethod
  def create_from_piece(cls, piece: Piece):
      cls._id = piece._id
      cls._name = piece.name
      cls._ransom = piece.rank.ransom
      cls._team_id = piece.team.id
      cls._team_name = piece.team.schema.name
      cls._rank_name = piece.rank.name
      cls._current_position = piece.current_position

      for discovery in piece.discoveries:
          cls._discoveries.append(DiscoveryDTO.create_from_discovery(discovery))

      if isinstance(piece, CombatantPiece) and piece.captor is not None:
          cls._captor_id = piece.captor.id
          cls._captor_name = piece.captor.name
      return cls

  def to_dict(self):
      return {
          "id": self._id,
          "name": self._name,
          "ransom": self._ransom,
          "team_id": self._team_id,
          "team_name": self._team_name,
          "rank_name": self._rank_name,
          "current_position": self._current_position,
          "captor_id": self._captor_id,
  }



