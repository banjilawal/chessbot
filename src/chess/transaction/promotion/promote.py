from typing import Generic, TypeVar, cast

from assurance.exception.invalid_id import IdValidationException
from chess.piece.model.exception import PieceValidationException
from assurance.exception.invalid_request import PromotionRequestValidationException

from chess.system.transaction.result import TransactionResult
from chess.system.id.validator import IdValidator
from chess.piece.validation.piece import PieceValidator
from chess.rank.queen import PromotedQueen
from chess.transaction.validators.base import RequestValidator
from chess.system.permit import Event
from chess.transaction.null_occupation_request import NullPromotionRequestException
from chess.exception.piece_exception import DoublePromotionException
from chess.exception.rank_exception import UnPromotableRankException, PromotionRowException


T = TypeVar('T')

class PromotionRequestValidator(RequestValidator):

  @staticmethod
  def validate(t: Generic[T]) -> TransactionResult:
    entity = "Promote"
    class_name = f"{entity}Validator"
    method = f"{class_name}.validate"

    """
    Validates an Promote meets specifications:
      - Not null
      - id does not validator
      - actor_candidate is team valid chess enemy
      - target is team valid square
    If team condition is not met an PromotionRequestValidationException will be thrown.

    Argument:
      candidate (Promote): Promote to validate

     Returns:
       Result[T]: A Result object containing the validated payload if the specification is satisfied,
        PromotionRequestValidationException otherwise.

    Raises:
      TypeError: if candidate is not Square
      NullPromotionRequestException: if candidate is null  

      InvalidIdException: if invalid id
      PieceValidationException: if candidate.actor_candidate fails validator
      
      PromotionRowException: if enemy is not on its enemy's validate row
      DoublePromotionException: if the enemy has already been promoted
      UnPromotableRankException: if the enemy's validate is not Pawn or King

      PromotionRequestValidationException: Wraps any preceding exceptions   
    """
    try:
      if t is None:
        raise NullPromotionRequestException(f"{method} {NullPromotionRequestException.DEFAULT_MESSAGE}")

      if not isinstance(t, PromotionRequest):
        raise TypeError(f"{method} Expected an Promote, got {type(t).__name__}")

      promotion_request = cast(PromotionRequest, t)

      id_result = IdValidator.validate(promotion_request.id)
      if not id_result.is_success():
        raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

      piece_result = PieceValidator.validate(promotion_request.actor)
      if not piece_result.is_success():
        raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

      piece = piece_result.payload
      if not isinstance(piece.rank, PromotedQueen):
        raise UnPromotableRankException(f"{method}: {UnPromotableRankException.DEFAULT_MESSAGE}")

      promotable = cast(piece, PromotedQueen)

      if promotable.rank.previous_rank is not None:
        raise DoublePromotionException(f"{method}: {DoublePromotionException.DEFAULT_MESSAGE}")

      current_row = piece.current_coordinate.row
      if current_row != piece.team.schema.enemy_home().rank_row :
        raise PromotionRowException(f"{method}: {PromotionRowException.DEFAULT_MESSAGE}")

      return TransactionResult(
        request=promotion_request,
        event=Event.PROMOTION
      )

    except (
      TypeError,
      PieceValidationException,
      NullPromotionRequestException,
      PromotionRowException,
      DoublePromotionException,
      UnPromotableRankException
    ) as e:
      raise PromotionRequestValidationException(
        f"{method}: {PromotionRequestValidationException.DEFAULT_MESSAGE}"
      ) from e
