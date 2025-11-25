# src/chess/team/context/exception.py

"""
Module: chess.team.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.rank import Rank
from chess.system import Context

class TeamContext(Context):

  _name: Optional[str] = None
  _rank: Optional[Rank] = None
  _ransom: Optional[int] = None,
  _piece_id: Optional[int] = None
  _roster_number: Optional[int] = None

  def __init__(
      self,
      name: Optional[str] = None,
      rank: Optional[Rank] = None,
      ransom: Optional[int] = None,
      piece_id: Optional[int]=None,
      roster_number: Optional[int]=None
  ):
    self._name = name
    self._rank = rank
    self._ransom = ransom
    self._piece_id = piece_id
    self._roster_number = roster_number
