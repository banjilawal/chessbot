from typing import Generic, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.piece import PieceValidationException
from assurance.exception.validation.request import AttackRequestValidationException
from assurance.exception.validation.square import SquareValidationException
from assurance.result.base import Result
from assurance.result.event import RequestOutcome

from assurance.validators.piece import PieceValidator
from chess.request.validators.base import RequestValidator
from assurance.validators.square import SquareValidator
from chess.exception.null.request import NullAttackRequestException
from chess.request.attack import AttackRequest


class AttackRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> RequestOutcome:
        entity = "AttackRequest"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an AttackRequest meets specifications:
            - Not null
            - id does not validation
            - client is a valid chess piece
            - resource is a valid square
        If a condition is not met an AttackRequestValidationException will be thrown.
        
        Argument:
            t (AttackRequest): attackRequest to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                AttackRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullAttackRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.client fails validation
            SquareValidationException: if it.resource fails validation

            AttackRequestValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullAttackRequestException(f"{method} {NullAttackRequestException.DEFAULT_MESSAGE}" )

            if not isinstance(t, AttackRequest):
                raise TypeError(f"{method} Expected an AttackRequest, got {type(t).__name__}")

            attack_request = cast(AttackRequest, t)

            id_result = IdValidator.validate(attack_request.id)
            if not id_result.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            piece_result = PieceValidator.validate(attack_request.client)
            if not piece_result.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

            square_result = SquareValidator.validate(attack_request.resource)
            if not square_result.is_success():
                raise SquareValidationException(f"{method}: {SquareValidationException.DEFAULT_MESSAGE}")

            return Result(payload=attack_request)

        except (
            TypeError,
            PieceValidationException,
            SquareValidationException,
            NullAttackRequestException
        ) as e:
            raise AttackRequestValidationException(
                f"{method}: {AttackRequestValidationException.DEFAULT_MESSAGE}"
            ) from e