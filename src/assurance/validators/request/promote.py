from typing import Generic, TypeVar, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.piece import PieceValidationException
from assurance.exception.validation.request import PromotionRequestValidationException
from assurance.exception.validation.square import SquareValidationException
from assurance.result.base import Result
from assurance.validators.id import IdValidator
from assurance.validators.piece import PieceValidator
from assurance.validators.request.base import RequestValidator
from chess.exception.null.request import NullPromotionRequestException
from chess.rank.promote import PromotableRank
from chess.request.promote import PromotionRequest

T = TypeVar('T')

class PromotionRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[PromotionRequest]:
        entity = "PromotionRequest"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an PromotionRequest meets specifications:
            - Not null
            - id does not validation
            - client is a valid chess piece
            - resource is a valid square
        If a condition is not met an PromotionRequestValidationException will be thrown.

        Argument:
            t (PromotionRequest): PromotionRequest to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                PromotionRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullPromotionRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.client fails validation

            PromotionRequestValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullPromotionRequestException(f"{method} {NullPromotionRequestException.DEFAULT_MESSAGE}")

            if not isinstance(t, PromotionRequest):
                raise TypeError(f"{method} Expected an PromotionRequest, got {type(t).__name__}")

            promotion_request = cast(PromotionRequest, t)

            id_result = IdValidator.validate(promotion_request.id)
            if not id_result.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            piece_result = PieceValidator.validate(promotion_request.client)
            if not piece_result.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

            piece = piece_result.payload
            if not isinstance(piece.rank, PromotableRank):
                raise Exception()

            current_row = piece.current_coordinate.row
            if current_row != piece.team.enemy_back_row_index()
                raise Exception()

            return Result(payload=promotion_request)

        except (
                TypeError,
                PieceValidationException,
                SquareValidationException,
                NullPromotionRequestException
        ) as e:
            raise PromotionRequestValidationException(
                f"{method}: {PromotionRequestValidationException.DEFAULT_MESSAGE}"
            ) from e
