# src/chess/piece/search/discoverySearchContext.py

"""
Module: chess.piece.search.discoverySearchContext
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.rank import Rank
from chess.system import SearchContext

class DiscoverySearchContext(SearchContext):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `DiscoverySearchContext` instances.
  2. Create new `DiscoverySearchContext` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `DiscoverySearchContext` or error information.

  # ATTRIBUTES:
  None
  """
  _name: Optional[str] = None
  _ransom: Optional[int] = None
  _piece_id: Optional[int] = None
  _team_id: Optional[id] = None
  _team_name: Optional[str] = None
  _rank_name: Optional[str] = None
  _position: Optional[Coord] = None

  def __init__(
      self,
      name: Optional[str] = None,
      ransom: Optional[int] = None,
      piece_id: Optional[int] = None,
      team_id: Optional[id] = None,
      team_name: Optional[str] = None,
      rank_name: Optional[Rank] = None,
      position: Optional[Coord] = None,
  ):
    self._name = name
    self._ransom = ransom
    self._piece_id = piece_id
    self._team_id = team_id
    self._team_name = team_name
    self._rank_name = rank_name
    self._position = position

  @property
  def name(self) -> Optional[str]:
    return self._name

  @property
  def ransom(self) -> Optional[int]:
    return self._ransom

  @property
  def piece_id(self) -> Optional[int]:
    return self._piece_id

  @property
  def team_id(self) -> Optional[int]:
    return self._team_id

  @property
  def team_name(self) -> Optional[str]:
    return self._team_name

  @property
  def rank_name(self) -> Optional[Rank]:
    return self._rank_name

  @property
  def position(self) -> Optional[Coord]:
    return self._position

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