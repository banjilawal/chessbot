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
  return self._name

@property
def rank(self) -> Optional[Rank]:
  return self._rank

@property
def ransom(self) -> Optional[int]:
  return self._ransom

@property
def piece_id(self) -> Optional[int]:
  return self._piece_id

@property
def roster_number(self) -> Optional[int]:
  return self._roster_number



def to_dict(self) -> dict:
  return {
    "name": self._name,
    "rank": self._rank,
    "ransom": self._ransom,
    "piece_id": self._piece_id,
    "roster_number": self._roster_number,
  }