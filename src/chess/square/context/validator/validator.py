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
    SquareContextValidationFailedException, ZeroSquareContextFlagsException, SquareContext,
    NullSquareContextException, ExcessiveSquareContextFlagsException, SquareContextValidationRouteException
)
from chess.token import TokenService


class SquareContextValidator(Validator[SquareContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a SquareContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

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
            token_service: TokenService = TokenService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[SquareContext]:
        """
        # ACTION:
            1.  If Candidate fails existence or type checks return the exception chain in the ValidationResult. Else,
                test how many optional attributes are not null.
            2.  If only one attribute is one and only one attribute is not null return the exception chain in the
                ValidationResult.
            3.  If no route is found for the enabled attribute send an exception chain in the ValidationResult.
            4.  If a validation route exists return the outcome of the validation to the caller.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   token_service (TokenService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   ValidationResult[SquareContext] containing either:
                    - On failure:   Exception.
                    - On success:   SquareContext in the payload.
        # RAISES:
            *   TypeError
            *   NullSquareContextException
            *   ZeroSquareContextFlagsException
            *   ExcessiveSquareContextFlagsException
            *   SquareContextValidationRouteException
            *   SquareContextValidationFailedException
        """
        method = "SquareContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationFailedException(
                    message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullSquareContextException(f"{method}: {NullSquareContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationFailedException(
                    message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Was expecting a SquareContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to SquareContext for additional tests. ---#
        context = cast(SquareContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationFailedException(
                    message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroSquareContextFlagsException(f"{method}: {ZeroSquareContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationFailedException(
                    message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveSquareContextFlagsException(
                        f"{method}: {ExcessiveSquareContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation = identity_service.validate_id(candidate=context.id)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationFailedException(
                        message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-name target.
        if context.name is not None:
            validation = identity_service.validate_name(context.name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationFailedException(
                        message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the name_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-coord target.
        if context.coord is not None:
            validation = coord_service.validator.validate(context.coord)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationFailedException(
                        message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the coord_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation = board_service.validator.validate(context.board)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationFailedException(
                        message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-token target.
        if context.token is not None:
            validation = token_service.validator.validate(context.token)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationFailedException(
                        message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            SquareContextValidationFailedException(
                message=f"{method}: {SquareContextValidationFailedException.DEFAULT_MESSAGE}",
                ex=SquareContextValidationRouteException(
                    f"{method}: {SquareContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )

