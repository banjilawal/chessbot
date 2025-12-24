# src/chess/persona/key/validator/validator.py

"""
Module: chess.persona.key.validator.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.persona import (
    PersonaSuperKey, InvalidPersonaSuperKeyException, NullPersonaSuperKeyException,
    ExcessivePersonaSuperKeyFlagsException, ZeroPersonaSuperKeyFlagsException
)
from chess.system import IdentityService, LoggingLevelRouter, NumberValidator, ValidationResult, Validator


class PersonaSuperKeyValidator(Validator[PersonaSuperKey]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a BattlePersona instance is certified safe, reliable and consistent before use.
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
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[PersonaSuperKey]:
        """
        # Action:
        1.  Confirm that only one in the (designation, quota, ransom) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's validator.
        3.  If any check fails return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an PersonaSuperKey are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   not_negative_validator (RansomValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[PersonaSuperKey] containing either:
            - On success: PersonaSuperKey in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullPersonaSuperKeyException
            *   ZeroPersonaFlagsException
            *   ExcessivePersonaSuperKeyFlagsException
            *   InvalidPersonaSuperKeyException
        """
        method = "PersonaSuperKeyValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullPersonaSuperKeyException(f"{method}: {NullPersonaSuperKeyException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an PersonaSuperKey validation has failed.
            if not isinstance(candidate, PersonaSuperKey):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected PersonaSuperKey, got {type(candidate).__designation__} instead.")
                )
            
            # Once existence and type checks are passed, cast the candidate to BattlePersona and run structure tests.
            context = cast(PersonaSuperKey, candidate)
            
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroPersonaSuperKeyFlagsException(f"{method}: {ZeroPersonaSuperKeyFlagsException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessivePersonaSuperKeyFlagsException(
                        f"{method}: {ExcessivePersonaSuperKeyFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # When structure tests are passed certify whichever search value was provided.
            
            # Certification for the search-by-name target.
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_persona.name map in a ValidationResult.
                return ValidationResult.success(context)
            
            # Certification for the search-by-designation target.
            if context.designation is not None:
                validation = identity_service.validate_name(candidate=context.designation)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_persona.designation map in a ValidationResult.
                return ValidationResult.success(context)
            
            # Certification for the search-by-quota target.
            if context.quota is not None:
                validation = number_validator.validate(candidate=context.quota)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_persona.quota map in a ValidationResult.
                return ValidationResult.success(context)
            
            # Certification for the search-by-ransom target.
            if context.ransom is not None:
                validation = number_validator.validate(candidate=context.ransom)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the battle_persona.ransom map in a ValidationResult.
                return ValidationResult.success(context)
        
        # Finally, catch any missed exception, wrap an InvalidPersonaSuperKeyException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPersonaSuperKeyException(
                    ex=ex, message=f"{method}: {InvalidPersonaSuperKeyException.DEFAULT_MESSAGE}"
                )
            )