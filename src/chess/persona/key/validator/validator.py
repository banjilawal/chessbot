# src/chess/persona/key/validator/validator.py

"""
Module: chess.persona.key.validator.validator
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from chess.persona import (
    ExcessivePersonaKeysException, NullPersonaKeyException, PersonaKey, ZeroPersonaKeysException,
    PersonaKeyValidationFailedException, PersonaKeyValidationRouteException
)
from chess.system import (
    IdentityService, LoggingLevelRouter, NumberValidator, ValidationFailedException, ValidationResult, Validator
)


class PersonaKeyValidator(Validator[PersonaKey]):
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
    ) -> ValidationResult[PersonaKey]:
        """
        # ACTION:
            1.  If the candidate passes existence and type checks cast into a PersonaKey instance, super_key.
                Else, return an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null return an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Persona.VARIANT.attribute == super_key.attribute return an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
        # RETURNS:Confirm
            *   ValidationResult[PersonaKey] containing either:
                    - On failure: Exception.
                    - On success: PersonaKey in the payload.
        # RAISES:
            *   TypeError
            *   NNullPersonaKeyException
            *   ZeroPersonaKeysException
            *   ExcessivePersonaKeysException
            *   PersonaKeyValidationFailedException
        """
        method = "PersonaKeyValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidationFailedException(
                    message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                    ex=NullPersonaKeyException(f"{method}: {NullPersonaKeyException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, PersonaKey):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidationFailedException(
                    message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected PersonaKey, got {type(candidate).__designation__} instead.")
                )
            )
        
        # After existence and type checks cast the candidate to a PersonaKey for additional tests.
        super_key = cast(PersonaKey, candidate)
        
        # Handle the case of searching with no attribute-value.
        if len(super_key.to_dict()) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidationFailedException(
                    message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                    ex=ZeroPersonaKeysException(f"{method}: {ZeroPersonaKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of more than one key-value is set.
        if len(super_key.to_dict()) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidationFailedException(
                    message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                    ex=ExcessivePersonaKeysException(
                        f"{method}: {ExcessivePersonaKeysException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Certification for the lookup-by-name target.
        if super_key.name is not None:
            validation = identity_service.validate_name(candidate=super_key.name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidationFailedException(
                        message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the battle_persona.name in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-designation target.
        if super_key.designation is not None:
            validation = identity_service.validate_name(candidate=super_key.designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidationFailedException(
                        message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the battle_persona.designation in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-quota target.
        if super_key.quota is not None:
            validation = number_validator.validate(candidate=super_key.quota)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidationFailedException(
                        message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the battle_persona.quota in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-ransom target.
        if super_key.ransom is not None:
            validation = number_validator.validate(candidate=super_key.ransom)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidationFailedException(
                        message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the battle_persona.ransom in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # The default returns failure.
        return ValidationResult.failure(
            PersonaKeyValidationFailedException(
                message=f"{method}: {ValidationFailedException.ERROR_CODE}",
                ex=PersonaKeyValidationRouteException(
                    f"{method}: {PersonaKeyValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
