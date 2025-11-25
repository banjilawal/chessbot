# src/chess/team/context/exception.py

"""
Module: chess.team.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.rank import Rank
from chess.system import SearchContext

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

@property
def name(self) -> Optional[str]:
  return self._visitor_name

@property
def rank(self) -> Optional[Rank]:
  return self._rank_name

@property
def ransom(self) -> Optional[int]:
  return self._visitor_ransom

@property
def piece_id(self) -> Optional[int]:
  return self._visitor_id

@property
def roster_number(self) -> Optional[int]:
  return self._roster_number



def to_dict(self) -> dict:
  return {
    "visitor_name": self._visitor_name,
    "bounds": self._rank_name,
    "visitor_ransom": self._visitor_ransom,
    "visitor_id": self._visitor_id,
    "roster_number": self._roster_number,
  }