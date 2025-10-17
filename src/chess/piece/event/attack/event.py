from typing import Optional

from chess.board import Board
from chess.event import Event
from chess.square import Square
from chess.piece import Piece, CombatantPiece
from chess.piece.event import TravelEvent
from chess.system import AutoId


@AutoId
class AttackEvent(TravelEvent):
  id: int
  _actor_square: Square
  _enemy: CombatantPiece


  def __init__(
    self,
    actor: Piece,
    actor_square: Square,
    destination_square: Square,
    enemy_combatant: CombatantPiece,
    board: Board,
    parent: Optional[Event]=None
  ):
    super().__init__(
      actor=actor,
      parent=parent,
      destination_square=destination_square,
      execution_environment=board
    )
    self._actor_square = actor_square
    self._enemy_combatant = enemy_combatant


  @property
  def actor_square(self) -> Square:
    return self._actor_square


  @property
  def enemy_combatant(self) -> CombatantPiece:
    return self._enemy_combatant


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, AttackEvent):
        return self._id == other.id
    return False