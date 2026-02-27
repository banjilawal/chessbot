

from enum import Enum
from typing import cast

from chess.exception import SearchException
from chess.token.exception import PieceCapturingItSelfException
from chess.player.finder import BoardSearch
from chess.square import Square
from assurance import ThrowHelper
from chess.event import KingOccupationEvent, KingOccupationEventBuilderException, TargetSquareMismatchException
from chess.system import IdValidator, BuildResult, ExecutionContext
from chess.piece import Piece, PieceValidator, InvalidKingOccupationException, CombatantPiece, \
  CaptureFriendException, KingCaptureException


class KingOccupationEventBuilder(Enum):
  """"""

  @staticmethod
  def build(
    event_id: int,
    actor: Piece,
    enemy: Piece,
    destination_square: Square,
    context: ExecutionContext
  ) -> BuildResult[KingOccupationEvent]:


    method = "KingOccupationEventBuilder.builder"

    try:
      id_validation = IdValidator.validate(event_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_exception(KingOccupationEventBuilder, id_validation)


      actor_validation = PieceValidator.validate(actor)
      if not actor_validation.is_success():
        raise InvalidKingOccupationException(f"{method}: KingOccupationEvent actor_candidate failed validate")

      enemy_validation = PieceValidator.validate(enemy)
      if not enemy_validation.is_success():
        raise InvalidKingOccupationException(f"{method}: KingOccupationEvent enemy failed validate")

      if actor == enemy:
        ThrowHelper.log_and_raise_exception(
          KingOccupationEventBuilder,
          PieceCapturingItSelfException(PieceCapturingItSelfException.MSG)
        )

      search_result = BoardSearch.square_by_coord(coord=enemy.current_position, board=context.board)
      if not search_result.payload == destination_square:
        ThrowHelper.log_and_raise_exception(
          KingOccupationEventBuilder,
          TargetSquareMismatchException(
            f"{method}: {TargetSquareMismatchException.MSG}"
          )
        )

      search = BoardSearch.square_by_coord(coord=actor.current_position, board=context.board)
      if not search.is_success():
        ThrowHelper.log_and_raise_exception(
          KingOccupationEventBuilder,
          SearchException(f"{method}: {SearchException.MSG}")
        )
      actor_square = cast(Square, search.payload)

      if not actor.is_enemy(enemy):
        ThrowHelper.log_and_raise_exception(
          KingOccupationEventBuilder,
          CaptureFriendException(CaptureFriendException.MSG)
        )

      if not isinstance(enemy, CombatantPiece):
        ThrowHelper.log_and_raise_exception(
          KingOccupationEventBuilder,
          KingCaptureException(KingCaptureException.MSG)
        )

      return BuildResult(payload=KingOccupationEvent(
        event_id=event_id,
        actor=actor,
        enemy=enemy,
        actor_square=actor_square,
        destination_square=destination_square
        )
      )

    except Exception as e:
      raise KingOccupationEventBuilderException(f"{method}: {e}") from e



      