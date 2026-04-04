# src/logic/schema/validation/validation.py

"""
Module: logic.schema.validation
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import Any, cast

from catalog.schema import NullSchemaException, Schema, SchemaValidationException
from system import LoggingLevelRouter, ValidationResult, Validator


class SchemaValidator(Validator[Schema]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Schema instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any) -> ValidationResult[Schema]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Schema]:
        """
        Verify the Schema is safe before its used.
        
        Action:
            1.  Send the exception chain in the ValidationResult if either:
                    -   The candidate is null.
                    -   It's not a Schema.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Schema]
        Raises:
            TypeError
            NullSchemaException
            SchemaValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=SchemaValidationException.OP,
                    msg=SchemaValidationException.MSG,
                    err_code=SchemaValidationException.ERR_CODE,
                    rslt_type=SchemaValidationException.RSLT_TYPE,
                    ex=NullSchemaException(
                        msg=SchemaValidationException.MSG,
                        err_code=SchemaValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Schema):
            # Return the exception chain on failure
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=SchemaValidationException.OP,
                    msg=SchemaValidationException.MSG,
                    err_code=SchemaValidationException.ERR_CODE,
                    rslt_type=SchemaValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Schema, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(Schema, candidate))