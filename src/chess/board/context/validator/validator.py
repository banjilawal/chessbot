# src/chess/board/context.validator/validator.py

"""
Module: chess.board.context.validator.validator
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Any, cast

from chess.arena.service import ArenaService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.board import (
    BoardContextValidationFailedException, ZeroBoardContextFlagsException, BoardContext,
    NullBoardContextException, ExcessiveBoardContextFlagsException, BoardContextValidationRouteException
)


class BoardContextValidator(Validator[BoardContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a BoardContext instance is certified safe, reliable and consistent before use.
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
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[BoardContext]:
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
            *   arena_service (ArenaService)
            *   identity_service (IdentityService):
        # RETURNS:
            *   ValidationResult[BoardContext] containing either:
                    - On failure:   Exception.
                    - On success:   BoardContext in the payload.
        # RAISES:
            *   TypeError
            *   NullBoardContextException
            *   ZeroBoardContextFlagsException
            *   ExcessiveBoardContextFlagsException
            *   BoardContextValidationRouteException
            *   BoardContextValidationFailedException
        """
        method = "BoardContextValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationFailedException(
                    message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullBoardContextException(f"{method}: {NullBoardContextException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, BoardContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationFailedException(
                    message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Was expecting a BoardContext, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to BoardContext for additional tests. ---#
        context = cast(BoardContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationFailedException(
                    message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ZeroBoardContextFlagsException(f"{method}: {ZeroBoardContextFlagsException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationFailedException(
                    message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                    ex=ExcessiveBoardContextFlagsException(
                        f"{method}: {ExcessiveBoardContextFlagsException.DEFAULT_MESSAGE}"
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
                    BoardContextValidationFailedException(
                        message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the id_BoardContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Certification for the search-by-arena target.
        if context.arena is not None:
            validation = arena_service.validator.validate(context.arena)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    BoardContextValidationFailedException(
                        message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the arena_BoardContext in the ValidationResult.
            return ValidationResult.success(payload=context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            BoardContextValidationFailedException(
                message=f"{method}: {BoardContextValidationFailedException.DEFAULT_MESSAGE}",
                ex=BoardContextValidationRouteException(
                    f"{method}: {BoardContextValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )