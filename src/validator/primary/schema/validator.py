# src/certifier/schema/validator.py

"""
Module: certifier.schema.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from validator import Certifier


class SchemaCertifier(Certifier[SchemaKey]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a SchemaKey instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[SchemaKey]:
        """
        # ACTION:
            1.  If the rank passes existence and type checks cast into a SchemaKey instance, super_key.
                Else, return an exception in the ValidationResult.
            2.  If one-and-only-one super_key field is not null return an exception in the ValidationResult.
            3.  Use super_key.attribute to route to the appropriate validation subflow.
            4.  If no Schema.VARIANT.attribute == super_key.attribute return an exception in the ValidationResult.
            5.  All tests are passed. Send super_key in the ValidationResult.
        # PARAMETERS:
            *   rank (Any)
            *   color_validator (ColorValidator)
            *   identity_service (IdentityService)
        # RETURNS:Confirm
            *   ValidationResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        Raises:
            *   TypeError
            *   NNullSchemaKeyException
            *   ZeroSchemaKeysException
            *   ArenaSchemaKeysException
            *   SchemaKeyValidatorException
        """
        method = "SchemaCertifier.execute"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidatorException(
                    msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                    ex=NullSchemaKeyException(f"{method}: {NullSchemaKeyException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SchemaKey):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidatorException(
                    msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                    ex=TypeError(f"{method}: Expected SchemaKey, got {type(candidate).__name__} instead.")
                )
            )
        
        # After existence and type checks cast the candidate into a SchemaKey for additional tests.
        super_key = cast(SchemaKey, candidate)
        
        # Handle the case of searching with no key-value is set.
        size = len(super_key.to_dict())
        if size  == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidatorException(
                    msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.MSG}")
                )
            )
        # Handle the case of more than one key-value is set.
        if size > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaKeyValidatorException(
                    msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                    ex=ArenaSchemaKeysException(
                        f"{method}: {ArenaSchemaKeysException.MSG}"
                    )
                )
            )
        
        # Route to the appropriate validation branch.
        
        # Certification for lookup-by-schema value.
        if super_key.designation is not None:
            validation = identity_service.validate_name(candidate=super_key.designation)
            # Send the exception chain on failure.
            if validation.is_failure:
                return ValidationResult.failure(
                    SchemaKeyValidatorException(
                        msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the SchemaMap_name in a ValidationResult.
            return ValidationResult.success(payload=super_key)
        
        # Certification for lookup-by-color value.
        if super_key.color is not None:
            validation = color_validator.execute(candidate=super_key.color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaKeyValidatorException(
                        msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                        ex=validator.exception
                    )
                )
            # On certification success return the SchemaMap_color in a ValidationResult.
            return ValidationResult.success(payload=super_key)
        
        # The default returns failure.
        return ValidationResult.failure(
            SchemaKeyValidatorException(
                msg=f"{method}: {SchemaKeyValidatorException.ERR_CODE}",
                ex=SchemaKeyValidationRouteException(
                    f"{method}: {SchemaKeyValidationRouteException.ERR_CODE}"
                )
            )
        )