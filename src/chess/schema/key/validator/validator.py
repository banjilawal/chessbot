# src/chess/schema/key/validator/validator.py

"""
Module: chess.schema.key.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Any, cast


from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.schema import (
    ExcessiveSchemaKeysException, NullSchemaKeyException, SchemaKey,
    SchemaKeyValidationException,
    SchemaKeyValidationRouteException, ZeroSchemaKeysException
)


class SchemaKeyValidator(Validator[SchemaKey]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a SchemaKey instance is certified safe, reliable and consistent before use.
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
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[SchemaKey]:
        """
        # ACTION:
            1.  If the candidate passes existence and type checks cast into a SchemaKey instance, super_key.
                Else, return an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null return an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Schema.VARIANT.attribute == super_key.attribute return an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
        # RETURNS:Confirm
            *   ValidationResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        # RAISES:
            *   TypeError
            *   NNullSchemaKeyException
            *   ZeroSchemaKeysException
            *   ExcessiveSchemaKeysException
            *   SchemaKeyValidationException
        """
        method = "SchemaKeyValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidationException(
                    message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                    ex=NullSchemaKeyException(f"{method}: {NullSchemaKeyException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SchemaKey):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidationException(
                    message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected SchemaKey, got {type(candidate).__name__} instead.")
                )
            )
        
        # After existence and type checks cast the candidate to a SchemaKey for additional tests.
        super_key = cast(SchemaKey, candidate)
        
        # Handle the case of searching with no key-value is set.
        size = len(super_key.to_dict())
        if size  == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidationException(
                    message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case of more than one key-value is set.
        if size > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidationException(
                    message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                    ex=ExcessiveSchemaKeysException(
                        f"{method}: {ExcessiveSchemaKeysException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Certification for lookup-by-name value.
        if super_key.name is not None:
            validation = identity_service.validate_name(candidate=super_key.name)
            # Return the exception chain on failure.
            if validation.is_failure:
                return ValidationResult.failure(
                    SchemaKeyValidationException(
                        message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the SchemaMap_name in a ValidationResult.
            return ValidationResult.success(payload=super_key)
        
        # Certification for lookup-by-color value.
        if super_key.color is not None:
            validation = color_validator.validate(candidate=super_key.color)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    SchemaKeyValidationException(
                        message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            # On certification success return the SchemaMap_color in a ValidationResult.
            return ValidationResult.success(payload=super_key)
        
        # The default returns failure.
        return ValidationResult.failure(
            SchemaKeyValidationException(
                message=f"{method}: {SchemaKeyValidationException.ERROR_CODE}",
                ex=SchemaKeyValidationRouteException(
                    f"{method}: {SchemaKeyValidationRouteException.ERROR_CODE}"
                )
            )
        )