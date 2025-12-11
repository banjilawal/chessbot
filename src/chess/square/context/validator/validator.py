# src/chess/square/context/validator/validator.py

"""
Module: chess.square.context.validator.validator
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Any, cast

from chess.board import BoardService
from chess.coord.service import CoordService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.square import (
    InvalidSquareContextException, NoSquareContextFlagSetException, NullSquareContextException,
    SquareContext, TooManySquareContextFlagsSetException
)


class SquareContextValidator(Validator[SquareContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Square instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * SquareValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            idservice: IdentityService = IdentityService()
    ) -> ValidationResult[SquareContext]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a SquareContext. If so cast it.
        3.  Verify only one flag is set.
        4.  For whichever of the flag is set certify its correctness with either validators in:
            BoardService, CoordService or IdentityService.
        5.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the SquareContext object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService):

        # Returns:
        ValidationResult[SquareContext] containing either:
            - On success:   SquareContext in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullSquareContextException
            *   InvalidSquareContextException
        """
        method = "SquareContextValidator.validate"
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullSquareContextException(f"{method}: {NullSquareContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, SquareContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Was expecting a SquareContext, {type(candidate)} instead.")
                )
            # Cast after the null and type checks are passed so Square attributes can be checked.
            context = cast(SquareContext, candidate)
            flag_count = len(context.to_dict())
            
            # Handle the cases with the wrong flag counts. 
            if flag_count == 0:
                return ValidationResult.failure(
                    NoSquareContextFlagSetException(
                        f"{method}: {NoSquareContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )     
            if flag_count > 1:
                return ValidationResult.failure(
                    TooManySquareContextFlagsSetException(
                        f"{method}: {TooManySquareContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            # Pick the flag which was turned on 
            if context.id is not None:
                id_validation = idservice.validate_id(candidate=context.id)
                if id_validation.is_failure:
                    return ValidationResult.failure(id_validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.name is not None:
                name_validation = idservice.validate_name(context.name)
                if name_validation.is_failure:
                    return ValidationResult.failure(name_validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.coord is not None:
                coord_validation = coord_service.item_validator.validate(context.coord)
                if coord_validation.is_failure:
                    return ValidationResult.failure(coord_validation.exception)
                return ValidationResult.success(payload=context)
            
        # Finally, if there is an unhandled exception Wrap an InvalidSquareContextException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSquareContextException(
                    ex=ex, message=f"{method}: {InvalidSquareContextException.DEFAULT_MESSAGE}"
                )
            )
