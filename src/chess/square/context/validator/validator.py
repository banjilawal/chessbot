# src/chess/square/context/validator/validator.py

"""
Module: chess.square.context.validator.validator
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from chess.token import TokenService
from chess.board import BoardService
from chess.coord.service import CoordService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.square import (
    SquareContextValidationException, SquareValidator, ZeroSquareContextFlagsException, SquareContext,
    NullSquareContextException, ExcessSquareContextFlagsException, SquareContextValidationRouteException
)



class SquareContextValidator(Validator[SquareContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a SquareContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails send an exception detailing the failure.

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
            identity_service: IdentityService = IdentityService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> ValidationResult[SquareContext]:
        """
        # ACTION:
            1.  If the candidate fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast candidate to SquareContext
                instance context.
            2.  Send an exception chain in the ValidationResult if either
                    *   The id
                    *   The name
                    *   The coord
                    *   The state
                    *   The board
                    *   The occupant
                are is not certified as safe by their services, or there is no validation
                route for the context.
            3.  The context has been certified as safe, send the validation success result.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   coord_service (CoordService)
            *   identity_service: (IdentityService)
            *   square_validator (SquareValidator)
        # RETURNS:
            *   ValidationResult[SquareContext] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload
        # RAISES:
            *   TypeError
            *   NullSquareContextException
            *   ZeroSquareContextFlagsException
            *   ExcessSquareContextFlagsException
            *   SquareContextValidationRouteException
            *   SquareContextValidationException
        """
        method = "SquareContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                    ex=NullSquareContextException(f"{method}: {NullSquareContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                    ex=TypeError(
                        f"{method}: Was expecting a SquareContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to SquareContext for additional tests. ---#
        context = cast(SquareContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                    ex=ZeroSquareContextFlagsException(f"{method}: {ZeroSquareContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationException(
                    message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                    ex=ExcessSquareContextFlagsException(
                        f"{method}: {ExcessSquareContextFlagsException.DEFAULT_MESSAGE}"
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
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
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
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
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
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
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
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-occupant target.
        if context.occupant is not None:
            validation = token_service.validator.validate(context.occupant)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-state.
        if context.state is not None:
            validation = square_validator.validate_square_state(context.occupant)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SquareContextValidationException(
                        message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the board_SquareContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            SquareContextValidationException(
                message=f"{method}: {SquareContextValidationException.DEFAULT_MESSAGE}",
                ex=SquareContextValidationRouteException(
                    f"{method}: {SquareContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )

