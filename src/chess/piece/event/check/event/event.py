from typing import Optional


from chess.board import Board
from chess.square import Square
from chess.system import AutoId, Event
from chess.piece import KingPiece, Piece, CombatantPiece, TravelEvent


class CheckEvent(TravelEvent):
  _actor_square: Square
  _enemy_king: KingPiece


  def __init__(
    self,
    id: int,
    actor: Piece,
    actor_square: Square,
    king_square: Square,
    king_piece: KingPiece,
    board: Board,
    parent: Optional[Event]=None
  ):
    super().__init__(
      id=id,
      actor=actor,
      parent=parent,
      destination_square=king_square,
      execution_environment=board
    )
    self._actor_square = actor_square
    self._king_piece = king_piece


  @property
  def actor_square(self) -> Square:
    return self._actor_square


  @property
  def king_piece(self) -> KingPiece:
    return self._enemy_king

  @property
  def king_square(self) -> Square:
    return self.destination_square


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, CheckEvent):
        return True
    return False