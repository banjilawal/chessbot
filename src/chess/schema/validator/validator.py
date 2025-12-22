# src/chess/schema/validator/validator.py

"""
Module: chess.schema.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast, Any

from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.schema import Schema, InvalidSchemaException, NullSchemaException


class SchemaValidator(Validator[Schema]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Schema.
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
    def validate(cls, candidate: Any) -> ValidationResult[Schema]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check the candidate is a Schema enum
        3.  If both checks pass cast the candidate to a Schema and return in a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[Schema] containing either:
            - On success:   Schema in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullSchemaException
            *   InvalidSchemaException
        """
        method = "SchemaValidator.validate"
        try:
            # Verify the candidate exists
            if candidate is None:
                return ValidationResult.failure(
                    NullSchemaException(f"{method} {NullSchemaException.DEFAULT_MESSAGE}")
                )
            # Verify the candidate is a Schema instance.
            if not isinstance(candidate, Schema):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected Schema, got {type(candidate).__name__} instead.")
                )
            # If both verifications are passed cast the candidate and return in ValidationResult.
            return ValidationResult.success(cast(Schema, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidSchemaException around it
        # then return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSchemaException(ex=ex, message=f"{method} {InvalidSchemaException.DEFAULT_MESSAGE}")
            )
