from typing import List

from assurance import ThrowHelper

from chess.exception import NullNumberException
from chess.rank import Rank, RankValidator
from chess.coord import Coord, CoordValidator
from chess.piece import Discovery, NullDiscoveryException
from chess.system import IdValidator, NameValidator, SearchResult


class Discoveries:
  """
  A collection class for managing `Discovery` records.

  `Discoveries` encapsulates the list of `Discovery` objects observed by team `Piece`.
  It ensures safe recording (no duplicates, no nulls) and provides old_search and filter
  operations over the stored discoveries. This separation allows discover management
  to evolve independently of the `Piece` itself, while keeping the `Piece` interface clean.

  Each discover represents team snapshot of another piece found during play (through
  scanning, moving, or event attempts). By aggregating them, `Discoveries`
  provides both simple access (all discoveries) and targeted lookups (by id, name,
  coordinate, rank, or ransom).

  Attributes:
    _items (List[Discovery]): Internal list storing the recorded discoveries.
      Exposed externally only through safe, immutable accessors.

  Notes:
    - Validation of ids, names, coordinates, and ranks is delegated to their
     respective validators (`IdValidator`, `NameValidator`, `CoordValidator`,
     `RankValidator`).
    - Each method returns team `SearchResult` to provide consistent success/empty/err handling.
    - The collection enforces uniqueness and immutability at the discover level.
  """
  _items: List[Discovery]

  def __init__(self):
    self._items = []


  @property
  def items(self) -> List[Discovery]:
    return self._items


  def reset(self):
    self._items.clear()



  def find_by_id(self, piece_id: int) -> SearchResult[Discovery]:
    """Find team discover by the id"""
    method = "Discoveries.find_by_id"

    try:
      id_validation = IdValidator.validate(piece_id)
      if not id_validation.is_success():
        return SearchResult(exception=id_validation.exception)

      discovery = next((discovery for discovery in self._items if discovery.id == piece_id), None)
      if discovery is not None:
        return SearchResult(payload=discovery)

      # returns empty old_search transaction
      return SearchResult()
    except Exception as e:
      return SearchResult(exception=e)


  def find_by_piece_name(self, piece_name: str) -> SearchResult[Discovery]:
    """Find team discover by the name"""
    method = "Discoveries.find_by_piece_name"

    try:
      name_validation = NameValidator.validate(piece_name)
      if not name_validation.is_success():
        return SearchResult(exception=name_validation.exception)

      discovery = next(
        (discovery for discovery in self._items if discovery.name.upper() == piece_name.upper()),
        None
      )
      if discovery is not None:
        return SearchResult(payload=discovery)

      # returns empty old_search transaction
      return SearchResult()
    except Exception as e:
      return SearchResult(exception=e)


  def find_by_coord(self, coord: Coord) -> SearchResult[Discovery]:
    """Find team discover by the coord"""
    method = "Discoveries.find_by_coord"

    try:
      coord_validation = CoordValidator.validate(coord)
      if not coord_validation.is_success():
        return SearchResult(exception=coord_validation.exception)

      discovery = next((discovery for discovery in self._items if discovery.position == coord), None)
      if discovery is not None:
        return SearchResult(payload=discovery)

      # returns empty old_search transaction
      return SearchResult()
    except Exception as e:
      return SearchResult(exception=e)


  def select_by_ransom(self, ransom: int) -> SearchResult[List[Discovery]]:
    """Filter discoveries by team rank's ransom value"""
    method = "Discoveries.select_by_ransom"

    try:
      if ransom is None:
        return SearchResult(exception=NullNumberException(NullNumberException.DEFAULT_MESSAGE))

      matches = [discovery for discovery in self._items if discovery.ransom == ransom]
      return SearchResult(payload=matches)

    except Exception as e:
      return SearchResult(exception=e)


  def select_by_rank(self, rank: Rank) -> SearchResult[List[Discovery]]:
    """Filter discoveries by rank"""
    method = "Discoveries.select_by_rank"

    try:
      rank_validation = RankValidator.validate(rank)
      if not rank_validation.is_success():
        return SearchResult(exception=rank_validation.exception)

      matches = [discovery for discovery in self._items if discovery.rank_name.upper == rank.name.upper()]
      return SearchResult(payload=matches)

    except Exception as e:
      return SearchResult(exception=e)









