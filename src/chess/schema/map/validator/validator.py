# src/chess/schema/map/validator/validator.py

"""
Module: chess.schema.map.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Any, cast

from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.schema import (
    InvalidSchemaSuperKeyException, ZeroSchemaSuperKeysException, NNullSchemaSuperKeyException, SchemaSuperKey,
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
        1.
        1.  Confirm that only one in the (name, color) tuple is not null.
        2.  Certify the not-null key-value is safe using the appropriate services and validators.
        3.  If any check fais return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an SchemaSuperKey are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[SchemaSuperKey] containing either:
            - On success: SchemaSuperKey in the payload.
            - On failure: Exception.

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
                    NNullSchemaSuperKeyException(f"{method}: {NNullSchemaSuperKeyException.DEFAULT_MESSAGE}")
                )
            # Handle the wrong type case.
            if not isinstance(candidate, SchemaSuperKey):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected SchemaSuperKey, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate to a SchemaSuperKey
            # for additional tests.
            map = cast(SchemaSuperKey, candidate)
            
            # Handle the case of searching with no key-value is set.
            if len(map.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroSchemaSuperKeysException(f"{method}: {ZeroSchemaSuperKeysException.DEFAULT_MESSAGE}")
                )
            # Handle the case of more than one key-value is set.
            if len(map.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveSchemaSuperKeysException(
                        f"{method}: {ExcessiveSchemaSuperKeysException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Using the hash's key-value as an address, route to appropriate validation subflow.
            
            # Certification for the forward lookup-by-name value.
            if map.name is not None:
                validation = identity_service.validate_name(candidate=map.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the SchemaMap_name in a ValidationResult.
                return ValidationResult.success(payload=map)
            
            # Certification for the forward lookup-by-color value.
            if map.color is not None:
                validation = color_validator.validate(candidate=map.color)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the color_team_schema_super_key in a ValidationResult.
                return ValidationResult.success(payload=map)
            
        # Finally, catch any missed exception and wrap an InvalidSchemaSuperKeyException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSchemaSuperKeyException(
                    ex=ex, message=f"{method}: {InvalidSchemaSuperKeyException.DEFAULT_MESSAGE}"
                )
            )