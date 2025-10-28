# src/chess/piece/travel/occupation/combatant/builder.py

"""
Module: chess.piece.travel.occupation.combatant.builder
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from enum import Enum
from typing import cast

from chess.exception import SearchException
from chess.piece.model.exception import PieceCapturingItSelfException
from chess.commander.search import BoardSearch
from chess.piece.travel.occupation.combatant.event import CombatantOccupation
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


    method = "AttackEventBuilder.build"

    try:
      id_validation = IdValidator.validate(event_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_error(AttackEventBuilder, id_validation)


      actor_validation = PieceValidator.validate(actor)
      if not actor_validation.is_success():
        raise InvalidAttackException(f"{method}: AttackEvent actor_candidate failed validate")

      enemy_validation = PieceValidator.validate(enemy)
      if not enemy_validation.is_success():
        raise InvalidAttackException(f"{method}: AttackEvent enemy failed validate")

      if actor == enemy:
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          PieceCapturingItSelfException(PieceCapturingItSelfException.DEFAULT_MESSAGE)
        )

      search_result = BoardSearch.square_by_coord(coord=enemy.current_position, board=context.board)
      if not search_result.payload == destination_square:
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          TargetSquareMismatchException(
            f"{method}: {TargetSquareMismatchException.DEFAULT_MESSAGE}"
          )
        )

      search = BoardSearch.square_by_coord(coord=actor.current_position, board=context.board)
      if not search.is_success():
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          SearchException(f"{method}: {SearchException.DEFAULT_MESSAGE}")
        )
      actor_square = cast(Square, search.payload)

      if not actor.is_enemy(enemy):
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          CaptureFriendException(CaptureFriendException.DEFAULT_MESSAGE)
        )

      if not isinstance(enemy, CombatantPiece):
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          KingCaptureException(KingCaptureException.DEFAULT_MESSAGE)
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



      