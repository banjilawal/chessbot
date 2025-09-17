from typing import Generic, TypeVar, cast

from assurance.exception.invalid_id import IdValidationException
from chess.piece.exception.invalid_piece import PieceValidationException
from assurance.exception.invalid_request import PromotionRequestValidationException

from chess.action.result import OperationResult
from chess.common.id_validator import IdValidator
from chess.piece.validator import PieceValidator
from chess.rank.queen import PromotedQueen
from chess.action.validators.base import RequestValidator
from chess.common.permit import Event
from chess.action.null_occupation_request import NullPromotionRequestException
from chess.exception.piece_exception import DoublePromotionException
from chess.exception.rank_exception import UnPromotableRankException, PromotionRowException


T = TypeVar('T')

class PromotionRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> OperationResult:
        entity = "Promote"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an Promote meets specifications:
            - Not null
            - id does not validator
            - actor is a valid chess piece
            - target is a valid square
        If a condition is not met an PromotionRequestValidationException will be thrown.

        Argument:
            t (Promote): Promote to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                PromotionRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullPromotionRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.actor fails validator
            
            PromotionRowException: if piece is not on its enemy's validation row
            DoublePromotionException: if the piece has already been promoted
            UnPromotableRankException: if the piece's validation is not Pawn or King

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
            if current_row != piece.team.profile.enemy_home().rank_row :
                raise PromotionRowException(f"{method}: {PromotionRowException.DEFAULT_MESSAGE}")

            return OperationResult(
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
