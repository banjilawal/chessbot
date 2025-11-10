# src/chess/owner/dto/dto.py

"""
Module: chess.owner.dto.dto
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import Optional

from chess.rank import RankDTO
from chess.team import TeamDTO
from chess.coord import CoordDTO
from chess.piece import PieceDTO, DiscoveryDTO



class PieceDTO:
  _id: int
  _name: str
  _rank_dto: int
  _team_dto: TeamDTO
  _current_position_dto: CoordDTO
  _captor_name: Optional[str]
  _discoveries_dto: list[DiscoveryDTO]

  
  def __init__(
    self,
    id: int,
    name: str,
    rank_dto: RankDTO,
    team_dto: TeamDTO,
    discoveries_dto: list[DiscoveryDTO],
    current_position_dto: CoordDTO,
    captor_name: Optional[str] = None,
  ):
      self._id = id
      self._name = name
      self._rank_dto = rank_dto
      self._team_dto = team_dto.id
      self._discoveries_dto = discoveries_dto
      self._current_position = current_position_dto
      self._captor_name = captor_name

  def to_dict(self):
      return {
          "visitor_id": self._id,
          "visitor_name": self._name,
          "team_dto": self._team_dto,
          "rank_dto": self._rank_dto,
          "captor_name": self._captor_name,
          "current_position_dto": self._current_position_dto,
          "discoveries_dto": self._discoveries_dto,
  }



