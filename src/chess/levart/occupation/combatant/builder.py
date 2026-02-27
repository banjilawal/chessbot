# src/chess/owner/travel/occupation/combatant/compute.py

"""
Module: chess.owner.travel.occupation.combatant.builder
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from typing import cast

from chess.exception import SearchException
from chess.token.exception import PieceCapturingItSelfException
from chess.player.finder import BoardSearch
from chess.square import Square
from assurance import ThrowHelper
from chess.event import AttackEvent, AttackEventBuilderException, TargetSquareMismatchException
from chess.system import IdValidator, BuildResult, ExecutionContext
from chess.piece import Piece, PieceValidator, InvalidAttackException, CombatantPiece, \
  CaptureFriendException, KingCaptureException


class CombatantOccupationEventBuilder(Builder[CombatantOccupationEvent]):
  """"""

  @staticmethod
  def build(
    event_id: int,
    actor: Piece,
    enemy: Piece,
    destination_square: Square,
    context: ExecutionContext
  ) -> BuildResult[AttackEvent]:


    method = "AttackEventBuilder.builder"

    try:
      id_validation = IdValidator.validate(event_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_exception(AttackEventBuilder, id_validation)


      actor_validation = PieceValidator.validate(actor)
      if not actor_validation.is_success():
        raise InvalidAttackException(f"{method}: AttackEvent actor_candidate failed validate")

      enemy_validation = PieceValidator.validate(enemy)
      if not enemy_validation.is_success():
        raise InvalidAttackException(f"{method}: AttackEvent enemy failed validate")

      if actor == enemy:
        ThrowHelper.log_and_raise_exception(
          AttackEventBuilder,
          PieceCapturingItSelfException(PieceCapturingItSelfException.MSG)
        )

      search_result = BoardSearch.square_by_coord(coord=enemy.current_position, board=context.board)
      if not search_result.payload == destination_square:
        ThrowHelper.log_and_raise_exception(
          AttackEventBuilder,
          TargetSquareMismatchException(
            f"{method}: {TargetSquareMismatchException.MSG}"
          )
        )

      search = BoardSearch.square_by_coord(coord=actor.current_position, board=context.board)
      if not search.is_success():
        ThrowHelper.log_and_raise_exception(
          AttackEventBuilder,
          SearchException(f"{method}: {SearchException.MSG}")
        )
      actor_square = cast(Square, search.payload)

      if not actor.is_enemy(enemy):
        ThrowHelper.log_and_raise_exception(
          AttackEventBuilder,
          CaptureFriendException(CaptureFriendException.MSG)
        )

      if not isinstance(enemy, CombatantPiece):
        ThrowHelper.log_and_raise_exception(
          AttackEventBuilder,
          KingCaptureException(KingCaptureException.MSG)
        )

      return BuildResult(payload=AttackEvent(
        event_id=event_id,
        actor=actor,
        enemy=enemy,
        actor_square=actor_square,
        destination_square=destination_square
        )
      )

    except Exception as e:
      raise AttackEventBuilderException(f"{method}: {e}") from e



      