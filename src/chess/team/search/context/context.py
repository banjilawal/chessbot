# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * `OccupationTransaction`
"""

from typing import Optional

from chess.rank import Rank
from chess.system import SearchContext, FilterContext

class PieceSearchContext(SearchContext):
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  """
  _name: Optional[str]
  _piece_id: Optional[int]
  _roster_number: Optional[int]

  def __init__(
      self,
      name: Optional[str] = None,
      piece_id: Optional[int]=None,
      roster_number: Optional[int]=None
  ):
    self._name = name
    self._piece_id = piece_id
    self._roster_number = roster_number


@property
def piece_id(self) -> Optional[int]:
  return self._piece_id

@property
def roster_number(self) -> Optional[int]:
  return self._roster_number

@property
def name(self) -> Optional[str]:
  return self._name

def to_dict(self) -> dict:
  return {
    "name": self._name,
    "piece_id": self._piece_id,
    "roster_number": self._roster_number,
  }


class PieceFilterContext(FilterContext):
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  """
  _rank: Optional[Rank]
  _min_capture_value: Optional[int]
  _max_capture_value: Optional[int]


  def __init__(
      self,
      rank: Optional[Rank]=None,
      min_capture_value: Optional[int]=None,
      max_capture_value: Optional[int]=None,
  ):
    self._rank = rank
    self._min_capture_value = min_capture_value
    self._max_capture_value = max_capture_value

@property
def rank(self) -> Optional[Rank]:
  return self._rank

@property
def min_capture_value(self) -> Optional[int]:
  return self.__min_capture_value

@property
def max_capture_value(self) -> Optional[int]:
  return self.__max_capture_value

def to_dict(self) -> dict:
  return {
    "rank": self._rank,
    "min_capture_value": self._min_capture_value,
    "max_capture_value": self._max_capture_value,
  }



