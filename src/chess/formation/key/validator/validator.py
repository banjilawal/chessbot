# src/chess/formation/key/validator/validator.py

"""
Module: chess.formation.key.validator.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
# 


from typing import Any, cast

from chess.formation import (
    ExcessiveFormationSuperKeysException, FormationSuperKey, FormationSuperKeyValidationFailedException,
    FormationSuperKeyValidationRouteException, NullFormationSuperKeyException, ZeroFormationSuperKeysException
)
from chess.persona import PersonaService
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
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[FormationSuperKey]:
        """
        # ACTION:
            1.  If the candidate passes existence and type checks cast into a FormationSuperKey instance, super_key.
                Else, return an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null return an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Formation.VARIANT.attribute == super_key.attribute return an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   persona_service (PersonaService)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
        # RETURNS:Confirm
            *   ValidationResult[FormationSuperKey] containing either:
                    - On failure: Exception.
                    - On success: FormationSuperKey in the payload.
        # RAISES:
            *   TypeError
            *   NNullFormationSuperKeyException
            *   ZeroFormationSuperKeysException
            *   ExcessiveFormationSuperKeysException
            *   FormationSuperKeyValidationFailedException
        """
        method = "FormationSuperKeyValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                FormationSuperKeyValidationFailedException(
                    message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                    ex=NullFormationSuperKeyException(f"{method}: {NullFormationSuperKeyException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, FormationSuperKey):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                FormationSuperKeyValidationFailedException(
                    message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                    ex=TypeError(
                        f"{method}: Expected FormationSuperKey, got {type(candidate).__designation__} instead."
                    )
                )
            )
        
        # After existence and type checks cast the candidate to a FormationSuperKey for additional tests.
        super_key = cast(FormationSuperKey, candidate)
        
        # Handle the case of searching with no key-value is set.
        if len(super_key.to_dict()) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                FormationSuperKeyValidationFailedException(
                    message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                    ex=ZeroFormationSuperKeysException(f"{method}: {ZeroFormationSuperKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of more than one key-value is set.
        if len(super_key.to_dict()) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                FormationSuperKeyValidationFailedException(
                    message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                    ex=ExcessiveFormationSuperKeysException(
                        f"{method}: {ExcessiveFormationSuperKeysException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Certification for lookup-by-name value.
        if super_key.name is not None:
            validation = identity_service.validate_name(candidate=super_key.name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    FormationSuperKeyValidationFailedException(
                        message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the formationMap_name in a ValidationResult.
            return ValidationResult.success(super_key)

        # Certification for lookup-by-designation value.
        if super_key.designation is not None:
            validation = identity_service.validate_name(candidate=super_key.designation)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    FormationSuperKeyValidationFailedException(
                        message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the formationMap_designation in a ValidationResult.
            return ValidationResult.success(super_key)

        # Certification for the lookup-by-square_name target.
        if super_key.square_name is not None:
            validation = identity_service.validate_name(candidate=super_key.square_name)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    FormationSuperKeyValidationFailedException(
                        message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the formationMap_square_name in a ValidationResult.
            return ValidationResult.success(super_key)

        # Certification for the lookup-by-color target.
        if super_key.color is not None:
            validation = color_validator.validate(candidate=super_key.color)
            if validation.is_failure:
                return ValidationResult.failure(
                    FormationSuperKeyValidationFailedException(
                        message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the formationMap_color in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # Certification for the lookup-by-persona target.
        if super_key.persona is not None:
            validation = persona_service.validator.validate(candidate=super_key.persona)
            if validation.is_failure:
                return ValidationResult.failure(
                    FormationSuperKeyValidationFailedException(
                        message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the formationMap_persona in a ValidationResult.
            return ValidationResult.success(super_key)
        
        # The default path returns failure
        return ValidationResult.failure(
            FormationSuperKeyValidationFailedException(
                message=f"{method}: {FormationSuperKeyValidationFailedException.ERROR_CODE}",
                ex=FormationSuperKeyValidationRouteException(
                    f"{method}: {FormationSuperKeyValidationRouteException.DEFAULT_MESSAGE}"
                )
            )
        )