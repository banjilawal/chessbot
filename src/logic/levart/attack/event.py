# src/logic/owner/travel/attack/factory.py

"""
Module: `logic.owner.travel.attack.event`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from logic.board import Board
from logic.system import Event
from logic.square import Square
from logic.piece import Piece, CombatantPiece, TravelEvent

class AttackEvent(TravelEvent):
  _actor_square: Square
  _enemy_combatant: CombatantPiece


  def __init__(
    self,
    id: int,
    actor: Piece,
    actor_square: Square,
    enemy_square: Square,
    enemy_combatant: CombatantPiece,
    execution_environment: Board,
    parent: Optional[Event]=None
  ):
    super().__init__(
      id=id,
      actor=actor,
      parent=parent,
      actor_square=actor_square,
      destination_square=enemy_square,
      execution_environment=execution_environment
    )
    self._actor_square = actor_square
    self._enemy_combatant = enemy_combatant

  @property
  def actor_square(self) -> Square:
    return self._actor_square

  @property
  def enemy_combatant(self) -> CombatantPiece:
    return self._enemy_combatant
  
  @property
  def enemy_square(self) -> Square:
    return self.destination_square


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, AttackEvent):
        return True
    return False