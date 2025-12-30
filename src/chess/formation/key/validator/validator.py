# src/chess/formation/key/validator/validator.py

"""
Module: chess.formation.key.validator.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
# 


from typing import Any, cast

from chess.formation import FormationSuperKey
from chess.formation.key.validator.exception.debug.null import NullFormationSuperKeyException
from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator


class FormationSuperKeyValidator(Validator[FormationSuperKey]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a FormationSuperKey instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

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
    ) -> ValidationResult[FormationSuperKey]:
        """
        # Action:
        1.  Confirm that only one in the (designation, square_designation, color) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's validator.
        3.  If any check fails return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an FormationSuperKey are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[FormationSuperKey] containing either:
            - On success: FormationSuperKey in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullFormationSuperKeyException
            *   ZeroFormationSuperKeyFlagsException
            *   ExcessiveFormationSuperKeyFlagsException
            *   InvalidFormationSuperKeyException
        """
        method = "FormationSuperKeyValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullFormationSuperKeyException(f"{method}: {NullFormationSuperKeyException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an FormationSuperKey validation has failed.
            if not isinstance(candidate, FormationSuperKey):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected FormationSuperKey instance, got {type(candidate).__designation__} instead.")
                )

            # Once existence and type checks are passed, cast the candidate to FormationSuperKey and run structure tests.
            context = cast(FormationSuperKey, candidate)

            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoFormationSuperKeyFlagException(f"{method}: {NoFormationSuperKeyFlagException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveFormationSuperKeyFlagsException(
                        f"{method}: {ExcessiveFormationSuperKeyFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # When structure tests are passed certify whichever search value was provided.

            # Certification for the search-by-designation target.
            if context.designation is not None:
                validation = identity_service.validate_name(candidate=context.designation)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.designation map in a ValidationResult.
                return ValidationResult.success(context)

            # Certification for the search-by-square_name target.
            if context.square is not None:
                validation = identity_service.validate_name(candidate=context.square)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.square_name map in a ValidationResult.
                return ValidationResult.success(context)

            # Certification for the search-by-color target.
            if context.color is not None:
                validation = color_validator.validate(candidate=context.color)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_order.color map in a ValidationResult.
                return ValidationResult.success(context)

        # Finally, catch any missed exception, wrap an InvalidFormationSuperKeyException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidFormationSuperKeyException(
                    ex=ex, message=f"{method}: {InvalidFormationSuperKeyException.DEFAULT_MESSAGE}"
                )
            )