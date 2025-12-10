# src/chess/team/schema/context/validator.py

"""
Module: chess.team.schema.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import Any, cast

from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import (
    InvalidTeamSchemaContextException, NoTeamSchemaContextFlagException, NullTeamSchemaContextException,
    TeamSchemaContext, TooManyTeamSchemaContextFlagsException
)


class TeamSchemaContextValidator(Validator[TeamSchemaContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a TeamSchema instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT
        *   Validator

    # PROVIDES:
        * TeamSchemaValidator

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
            color_validator: GameColorValidator = GameColorValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[TeamSchemaContext]:
        """
        # Action:
        1.  Confirm that only one in the (name, color) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's validator.
        3.  If any check fais return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an TeamSchemaContext are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[TeamSchemaContext] containing either:
            - On success: TeamSchemaContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullTeamSchemaContextException
            *   NoTeamSchemaContextFlagException
            *   TooManyTeamSchemaContextFlagsException
            *   InvalidTeamSchemaContextException
        """
        method = "TeamSchemaContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamSchemaContextException(f"{method}: {NullTeamSchemaContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an TeamSchemaContext validation has failed.
            if not isinstance(candidate, TeamSchemaContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamSchemaContext, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed candidate can be cast to an TeamSchemaContext
            # For additional checks.
            context = cast(TeamSchemaContext, candidate)
            
            # Perform the two checks ensuring only one TeamSchema attribute value will be used in the searcher.
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoTeamSchemaContextFlagException(f"{method}: {NoTeamSchemaContextFlagException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyTeamSchemaContextFlagsException(
                        f"{method}: {TooManyTeamSchemaContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Which ever attribute value is not null should be certified safe by the appropriate validator.
            
            #
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.color is not None:
                validation = color_validator.validate(candidate=context.team)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidTeamSchemaContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamSchemaContextException(
                    ex=ex, message=f"{method}: {InvalidTeamSchemaContextException.DEFAULT_MESSAGE}"
                )
            )