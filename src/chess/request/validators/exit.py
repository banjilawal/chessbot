from typing import Generic, TypeVar, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.piece import PieceValidationException
from assurance.exception.validation.request import ExitRequestValidationException

from assurance.result.permission import PermissionResult
from assurance.validators.id import IdValidator
from assurance.validators.piece import PieceValidator
from chess.request.validators.base import RequestValidator
from chess.common.grant import Permission
from chess.exception.null.request import NullExitRequestException
from chess.request.exit import ExitRequest

T = TypeVar('T')

class ExitRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> PermissionResult:
        entity = "ExitRequest"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an ExitRequest meets specifications:
            - Not null
            - id is valid
            - client is a valid chess piece
        If a condition is not met an ExitRequestValidationException will be thrown.

        Argument:
            t (ExitRequest): ExitRequest to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                ExitRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullExitRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.client fails validation

            ExitRequestValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullExitRequestException(f"{method} {NullExitRequestException.DEFAULT_MESSAGE}")

            if not isinstance(t, ExitRequest):
                raise TypeError(f"{method} Expected an ExitRequest, got {type(t).__name__}")

            exit_request = cast(ExitRequest, t)

            id_result = IdValidator.validate(exit_request.id)
            if not id_result.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            piece_result = PieceValidator.validate(exit_request.client)
            if not piece_result.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

            return PermissionResult(request=exit_request, permission=Permission.GRANT_EXIT_PERMISSION)

        except (
            TypeError,
            IdValidationException,
            PieceValidationException,
            NullExitRequestException
        ) as e:
            raise ExitRequestValidationException(
                f"{method}: {ExitRequestValidationException.DEFAULT_MESSAGE}"
            ) from e
