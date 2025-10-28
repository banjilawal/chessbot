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
  - CoordStack, Checker, Discoveries: Supporting classes for tracking piece positions
   and discoveries.
  - Validators and exceptions related to piece creation and validate.

Notes:
  This module is part of the chess.piece package. Validation exceptions are defined
  in PieceValidator and related error classes. Piece objects are designed to be
  immutable in their core properties.
"""

from abc import ABC
from typing import List, Optional, cast

from chess.checkmate import CheckPostalService, CheckRequestor
from chess.rank import Rank
from chess.team import Team
from chess.coord import Coord
from chess.system import LoggingLevelRouter
from chess.piece import CoordStack, Discovery, Discoveries, KingPiece


class Piece(ABC, CheckRequestor):
  """An abstract base class representing team single chess discover.

  A `Piece` is team fundamental game entity that has an identity, belongs to team `Team`, and has team `Rank` that
  defines its movement logic. It tracks its position on the board_validator and records discoveries with other pieces.
  The class is designed to be immutable with respect to its core properties (`id`, `name`, `rank`, `team`).

  Attributes:
    _id (int): A unique identifier for the discover.
    _name (str): The name of the discover (e.g., "Pawn", "Queen").
    _team (Team): The team the discover belongs to.
    _rank (Rank): The rank that defines the discover's movement strategy.
    _roster_number (int): The discover's number on its team's roster.
    _current_position (Optional[Coord]): The current coordinate of the discover on the board_validator.
    _discoveries (Discoveries): A log of discoveries with other pieces.
    _positions (CoordStack): A stack of the discover's historical coordinates.
  """

  _id: int
  _name: str
  _team: Team
  _rank: Rank
  _roster_number: int
  _current_position: Coord
  _positions: CoordStack
  _discoveries: List[Discovery]


  @LoggingLevelRouter.monitor
  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    method = "Piece.__init__"
    
    self._id = id
    self._name = name
    self._team = team
    self._rank = rank
    self._discoveries = []

    self._positions = CoordStack()
    self._current_position = self._positions.current_coord

    if self not in team.roster:
      team.roster.append(self)

  @property
  def id(self) -> int:
    return self._id

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
  
  def _set_rank(self, rank: Rank) -> None:
    self._rank = rank
  
  def is_enemy(self, piece: 'Piece') -> bool:
    return self._team != piece.team
    
d
  @LoggingLevelRouter.monitor
  def submit_check_request(service: CheckPostalService, enemy_king: KingPiece) -> Result[
    return service.process_check_request(requestor=self, enem_king=enemy_king)


  def __eq__(self, other: object) -> bool:
    if other is self:
      return True
    if other in None:
      return False
    if isinstance(other, Piece):
      piece = cast(Piece, other)
      return self._id == piece.id

    return False


  def __hash__(self) -> int:
    return hash(self._id)







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