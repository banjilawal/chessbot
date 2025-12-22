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
    InvalidSchemaSuperKeyException, ZeroSchemaSuperKeysException, NullSchemaSuperKeyException, SchemaSuperKey,
    ExcessiveSchemaSuperKeysException
)

class SchemaSuperKeyValidator(Validator[SchemaSuperKey]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a SchemaSuperKey instance is certified safe, reliable and consistent before use.
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
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[SchemaSuperKey]:
        """
        # Action:
            1.  If the candidate passes existence and type checks cast into a SchemaSuperKey instance, super_key.
                Else, send an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null send an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Schema.VARIANT.attribute == super_key.attribute send an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:Confirm
        ValidationResult[SchemaSuperKey] containing either:
                - On failure: Exception.
                - On success: SchemaSuperKey in the payload.

        # Raises:
            *   TypeError
            *   NNullSchemaSuperKeyException
            *   ZeroSchemaSuperKeysException
            *   ExcessiveSchemaSuperKeysException
            *   InvalidSchemaSuperKeyException
        """
        method = "SchemaSuperKeyValidator.validate"
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(
                    NullSchemaSuperKeyException(f"{method}: {NullSchemaSuperKeyException.DEFAULT_MESSAGE}")
                )
            # Handle the wrong type case.
            if not isinstance(candidate, SchemaSuperKey):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected SchemaSuperKey, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks cast the candidate to a SchemaSuperKey for additional tests.
            super_key = cast(SchemaSuperKey, candidate)
            
            # Handle the case of searching with no key-value is set.
            size = len(super_key.to_dict())
            if size  == 0:
                return ValidationResult.failure(
                    ZeroSchemaSuperKeysException(f"{method}: {ZeroSchemaSuperKeysException.DEFAULT_MESSAGE}")
                )
            # Handle the case of more than one key-value is set.
            if size > 1:
                return ValidationResult.failure(
                    ExcessiveSchemaSuperKeysException(
                        f"{method}: {ExcessiveSchemaSuperKeysException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Route to the appropriate validation branch.
            
            # Certification for the forward lookup-by-name value.
            if super_key.name is not None:
                validation = identity_service.validate_name(candidate=super_key.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the SchemaMap_name in a ValidationResult.
                return ValidationResult.success(payload=super_key)
            
            # Certification for the forward lookup-by-color value.
            if super_key.color is not None:
                validation = color_validator.validate(candidate=super_key.color)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the SchemaMap_color in a ValidationResult.
                return ValidationResult.success(payload=super_key)
            
        # Finally, catch any missed exception, wrap an InvalidSchemaSuperKeyException it. Then send the exception-chain
        # in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSchemaSuperKeyException(
                    ex=ex, message=f"{method}: {InvalidSchemaSuperKeyException.DEFAULT_MESSAGE}"
                )
            )