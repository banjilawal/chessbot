# src/logic/persona/key/validator/validator.py

"""
Module: logic.persona.key.validator.validation
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Any, cast

from schema.persona import (
    ArenaPersonaKeysException, NullPersonaKeyException, PersonaKey, ZeroPersonaKeysException,
    PersonaKeyValidatorException, PersonaKeyValidationRouteException
)
from system import (
    IdentityService, LoggingLevelRouter, NumberValidator, ValidatorException, ValidationResult
)


class PersonaRootCertifier(RootCertifier[PersonaKey]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a BattlePersona instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    Provides:


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
            1.  If the rank passes existence and type checks cast into a PersonaBlueprint instance, super_key.
                Else, return an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null return an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Persona.VARIANT.attribute == super_key.attribute return an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.
        # PARAMETERS:
            *   rank (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
        # RETURNS:Confirm
            *   ValidationResult[Persona] containing either:
                    - On failure: Exception.
                    - On success: PersonaBlueprint in the payload.
        Raises:
            *   TypeError
            *   NNullPersonaKeyException
            *   ZeroPersonaKeysException
            *   ArenaPersonaKeysException
            *   PersonaKeyValidatorException
        """
        method = "POersonaBlueprint.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidatorException(
                    msg=f"{method}: {ValidatorException.ERR_CODE}",
                    ex=NullPersonaKeyException(f"{method}: {NullPersonaKeyException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, PersonaKey):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidatorException(
                    msg=f"{method}: {ValidatorException.ERR_CODE}",
                    ex=TypeError(f"{method}: Expected PersonaBlueprint, got {type(candidate).__designation__} instead.")
                )
            )
        
        # After existence and type checks cast the candidate into a PersonaBlueprint for additional tests.
        super_key = cast(PersonaKey, candidate)
        
        # Handle the case of searching with no attribute-value.
        if len(super_key.to_dict()) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidatorException(
                    msg=f"{method}: {ValidatorException.ERR_CODE}",
                    ex=ZeroPersonaKeysException(f"{method}: {ZeroPersonaKeysException.MSG}")
                )
            )
        # Handle the case of more than one key-value is set.
        if len(super_key.to_dict()) > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PersonaKeyValidatorException(
                    msg=f"{method}: {ValidatorException.ERR_CODE}",
                    ex=ArenaPersonaKeysException(
                        f"{method}: {ArenaPersonaKeysException.MSG}"
                    )
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Certification for the lookup-by-schema target.
        if super_key.designation is not None:
            validation = identity_service.validate_name(candidate=super_key.designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidatorException(
                        msg=f"{method}: {ValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the battle_persona.schema in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-designation target.
        if super_key.designation is not None:
            validation = identity_service.validate_name(candidate=super_key.designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidatorException(
                        msg=f"{method}: {ValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the battle_persona.designation in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-quota target.
        if super_key.quota is not None:
            validation = number_validator.execute(candidate=super_key.quota)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidatorException(
                        msg=f"{method}: {ValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the battle_persona.quota in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-ransom target.
        if super_key.ransom is not None:
            validation = number_validator.execute(candidate=super_key.ransom)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PersonaKeyValidatorException(
                        msg=f"{method}: {ValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the battle_persona.ransom in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # The default returns failure.
        return ValidationResult.failure(
            PersonaKeyValidatorException(
                msg=f"{method}: {ValidatorException.ERR_CODE}",
                ex=PersonaKeyValidationRouteException(
                    f"{method}: {PersonaKeyValidationRouteException.MSG}"
                )
            )
        )
