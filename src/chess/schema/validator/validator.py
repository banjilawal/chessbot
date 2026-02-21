# src/chess/schema/validator/validator.py

"""
Module: chess.schema.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.schema import Schema, SchemaValidationException, NullSchemaException


class SchemaValidator(Validator[Schema]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Schema.
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
    def validate(cls, candidate: Any) -> ValidationResult[Schema]:
        """
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Schema instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Schema] containing either:
                    - On failure: Exception.
                    - On success: Schema in the payload.
        # RAISES:
            *   TypeError
            *   NullSchemaException
            *   SchemaValidationException
        """
        method = "SchemaValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaValidationException(
                    message=f"{method}: {SchemaValidationException.ERROR_CODE}",
                    ex=NullSchemaException(f"{method} {NullSchemaException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Schema):
            # Return the exception chain on failure
            return ValidationResult.failure(
                SchemaValidationException(
                    message=f"{method}: {SchemaValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected a Schema, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the schema instance in a ValidationResult.
        return ValidationResult.success(payload=cast(Schema, candidate))
