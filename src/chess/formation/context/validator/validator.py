# src/chess/team/team_schema/context/validator.py

"""
Module: chess.team.team_schema.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Any, cast

from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.formation import (
    InvalidBattleOrderContextException, NoBattleOrderContextFlagException, NullBattleOrderContextException,
    BattleOrderContext, TooManyBattleOrderContextFlagsException
)


class BattleOrderContextValidator(Validator[BattleOrderContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a BattleOrder instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

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
            color_validator: GameColorValidator = GameColorValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[BattleOrderContext]:
        """
        # Action:
        1.  Confirm that only one in the (name, square_name, color) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's validator.
        3.  If any check fails return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an BattleOrderContext are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[BattleOrderContext] containing either:
            - On success: BattleOrderContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullBattleOrderContextException
            *   NoBattleOrderContextFlagException
            *   TooManyBattleOrderContextFlagsException
            *   InvalidBattleOrderContextException
        """
        method = "BattleOrderContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullBattleOrderContextException(f"{method}: {NullBattleOrderContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an BattleOrderContext validation has failed.
            if not isinstance(candidate, BattleOrderContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected BattleOrderContext, got {type(candidate).__name__} instead.")
                )
            
            # Once existence and type checks are passed, cast the candidate to BattleOrder and run structure tests.
            context = cast(BattleOrderContext, candidate)
            
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoBattleOrderContextFlagException(f"{method}: {NoBattleOrderContextFlagException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyBattleOrderContextFlagsException(
                        f"{method}: {TooManyBattleOrderContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # When structure tests are passed certify whichever search value was provided.
            
            # Certification for the search-by-name target.
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.name context in a ValidationResult.
                return ValidationResult.success(context)
            
            # Certification for the search-by-square target.
            if context.square is not None:
                validation = identity_service.validate_name(candidate=context.square)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.square context in a ValidationResult.
                return ValidationResult.success(context)
            
            # Certification for the search-by-color target.
            if context.color is not None:
                validation = color_validator.validate(candidate=context.color)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.color context in a ValidationResult.
                return ValidationResult.success(context)
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidBattleOrderContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidBattleOrderContextException(
                    ex=ex, message=f"{method}: {InvalidBattleOrderContextException.DEFAULT_MESSAGE}"
                )
            )