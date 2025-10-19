"""
Module: piece
Author: Banji Lawal
Created: 2025-09-28
Purpose:
  Defines the Piece class hierarchy for the chess engine, including abstract and
  concrete pieces such as KingPiece and CombatantPiece. Pieces track identity, team
  membership, rank, and board_validator position, and manage interactions with other pieces.

Contents:
  - Piece: Abstract base class representing team chess piece with position and rank.
  - KingPiece: Concrete subclass representing team king piece.
  - CombatantPiece: Concrete subclass representing team piece capable of capturing others.
  - CoordStack, Discovery, Discoveries: Supporting classes for tracking piece positions
   and discoveries.
  - Validators and exceptions related to piece creation and validate.

Notes:
  This module is part of the chess.piece package. Validation exceptions are defined
  in PieceValidator and related error classes. Piece objects are designed to be
  immutable in their core properties.
"""

from abc import ABC
from typing import List, Optional, cast

from chess.rank import Rank
from chess.team import Team
from chess.coord import Coord
from chess.system import AutoId, LoggingLevelRouter
from chess.piece import CoordStack, Discovery, Discoveries


__all__ = [
  'Piece',
  'KingPiece',
  'CombatantPiece'
]


@AutoId
class Piece(ABC):
  """An abstract base class representing team single chess discover.

  A `Piece` is team fundamental game entity that has an identity, belongs to team `Team`, and has team `Rank` that
  defines its movement logic. It tracks its position on the board_validator and records discoveries with other pieces.
  The class is designed to be immutable with respect to its core properties (`id`, `name`, `rank`, `team`).

  Attributes:
    _piece_id (int): A unique identifier for the discover.
    _name (str): The name of the discover (e.g., "Pawn", "Queen").
    _team (Team): The team the discover belongs to.
    _rank (Rank): The rank that defines the discover's movement strategy.
    _roster_number (int): The discover's number on its team's roster.
    _current_position (Optional[Coord]): The current coordinate of the discover on the board_validator.
    _discoveries (Discoveries): A log of discoveries with other pieces.
    _positions (CoordStack): A stack of the discover's historical coordinates.
  """

  id: int
  _name: str
  _team: Team
  _rank: Rank
  _roster_number: int
  _current_position: Coord
  _positions: CoordStack
  _discoveries: List[Discovery]


  @LoggingLevelRouter.monitor
  def __init__(self, name: str, rank: Rank, team: Team):
    method = "Piece.__init__"
    self._name = name
    self._team = team
    self._rank = rank
    self._discoveries = []

    self._positions = CoordStack()
    self._current_position = self._positions.current_coord

    if self not in team.roster:
      team.add_to_roster(self)


  # @property
  # def id(self) -> int:
  #   """The unique ID of the discover."""
  #   return self._piece_id


  @property
  def name(self) -> str:
    return self._name


  @property
  def roster_number(self) -> int:
    return self._roster_number


  @property
  def team(self) -> 'Team':
    return self._team


  @property
  def rank(self) -> 'Rank':
    return self._rank


  @property
  def positions(self) -> CoordStack:
    return self._positions


  @property
  def current_position(self) -> Optional[Coord]:
    return self._positions.current_coord


  @property
  def discoveries(self) -> List[Discovery]:
    return self._discoveries


  def __eq__(self, other: object) -> bool:
    if other is self:
      return True
    if other in None:
      return False
    if not isinstance(other, 'Piece'):
      return False
    return self.id == other.id


  def __hash__(self) -> int:
    """Returns the hash value of the Piece based on its ID."""
    return hash(self.id)


  def is_enemy(self, piece: 'Piece') -> bool:
    return self._team != piece.team


  def record_discovery(self, discovery: Discovery):
    if discovery not in self._discoveries:
      self._discoveries.record_discovery(discovery)



  def __str__(self) -> str:
    """Returns team string representation of the Piece."""
    return (
      f"Piece[id:{self._id} "
      f"name:{self._name} "
      f"rank:{self._rank.name} "
      f"team:{self._team.schema.name} "
      f"position:{self._positions.current_coord} "
      f"moves:{self._positions.size()}]"
    )


class KingPiece(Piece):
  """A concrete subclass representing team king piece."""
  _is_checked: bool
  _is_checkmated: bool

  def __init__(self,name: str, rank: 'Rank', team: 'Team'):
    super().__init__(name, rank, team)
    self._is_checked = False
    self._is_checkmated = False


  @property
  def is_checked(self) -> bool:
    return self._is_checked

  @property
  def is_checkmated(self) -> bool:
    return self._is_checkmated

  @is_checked.setter
  def is_checked(self, is_checked: bool):
    self._is_checked = is_checked

  @is_checkmated.setter
  def is_checkmated(self, is_checkmated: bool):
    if self._is_checked:
      self._is_checkmated = is_checkmated
    else:
      raise Exception("Cannot set checkmated status if not checked")


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, KingPiece):
      return self.id == other.id


class CombatantPiece(Piece):
  _captor: Optional[Piece]

  def __init__(self, name: str, rank: 'Rank', team: 'Team'):
    super().__init__(name, rank, team)
    self._captor = None


  @property
  def captor(self) -> Optional[Piece]:
    return self._captor


  @captor.setter
  def captor(self, captor: Piece):
    self._captor = captor


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, CombatantPiece):
      return self.id == other.id



