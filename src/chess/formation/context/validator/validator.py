# src/chess/formation/context/validator/validator.py

"""
Module: chess.formation.context.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Any, cast

from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.formation import (
    InvalidOrderContextException, NoOrderContextFlagException, NullOrderContextException, OrderContext,
    ExcessiveOrderContextFlagsException
)


class OrderContextValidator(Validator[OrderContext]):
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
    ) -> ValidationResult[OrderContext]:
        """
        # Action:
        1.  Confirm that only one in the (designation, square_designation, color) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's number_bounds_validator.
        3.  If any check fails return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an OrderContext are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[OrderContext] containing either:
            - On success: OrderContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullOrderContextException
            *   ZeroOrderContextFlagsException
            *   ExcessiveOrderContextFlagsException
            *   InvalidOrderContextException
        """
        method = "OrderContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullOrderContextException(f"{method}: {NullOrderContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an OrderContext validation has failed.
            if not isinstance(candidate, OrderContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected OrderContext, got {type(candidate).__designation__} instead.")
                )
            
            # Once existence and type checks are passed, cast the candidate to BattleOrder and run structure tests.
            context = cast(OrderContext, candidate)
            
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoOrderContextFlagException(f"{method}: {NoOrderContextFlagException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveOrderContextFlagsException(
                        f"{method}: {ExcessiveOrderContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # When structure tests are passed certify whichever search value was provided.
            
            # Certification for the search-by-designation target.
            if context.designation is not None:
                validation = identity_service.validate_name(candidate=context.designation)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.designation context in a ValidationResult.
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
        # an InvalidOrderContextException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidOrderContextException(
                    ex=ex, message=f"{method}: {InvalidOrderContextException.DEFAULT_MESSAGE}"
                )
            )