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
    InvalidSchemaMapException, ZeroSchemaMapKeysException, NullSchemaMapException, SchemaMap,
    ExcessiveSchemaMapKeysException
)


class SchemaMapValidator(Validator[SchemaMap]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Schema instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL KEY-VALUES:
    None

    # INHERITED KEY-VALUES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            color_validator: GameColorValidator = GameColorValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[SchemaMap]:
        """
        # Action:
        1.  Confirm that only one in the (name, color) hash is not null.
        2.  Certify the not-null key-value is safe using the appropriate services and validators.
        3.  If any check fais return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an SchemaMap are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[SchemaMap] containing either:
            - On success: SchemaMap in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullSchemaMapException
            *   ZeroSchemaMapKeysException
            *   ExcessiveSchemaMapKeysException
            *   InvalidSchemaMapException
        """
        method = "SchemaMapValidator.validate"
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(
                    NullSchemaMapException(f"{method}: {NullSchemaMapException.DEFAULT_MESSAGE}")
                )
            # Handle the wrong type case.
            if not isinstance(candidate, SchemaMap):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected SchemaMap, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate to a SchemaMap
            # for additional tests.
            map = cast(SchemaMap, candidate)
            
            # Handle the case of searching with no key-value is set.
            if len(map.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroSchemaMapKeysException(f"{method}: {ZeroSchemaMapKeysException.DEFAULT_MESSAGE}")
                )
            # Handle the case of more than one key-value is set.
            if len(map.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveSchemaMapKeysException(
                        f"{method}: {ExcessiveSchemaMapKeysException.DEFAULT_MESSAGE}"
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
                # On certification success return the color_team_schema_map in a ValidationResult.
                return ValidationResult.success(payload=map)
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidSchemaMapException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSchemaMapException(
                    ex=ex, message=f"{method}: {InvalidSchemaMapException.DEFAULT_MESSAGE}"
                )
            )