# src/chess/builder/validator.py

"""
Module: chess.builder.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    Builder, UnreliableBuilderException, LoggingLevelRouter, NullBuilderException, ValidationResult,
    Validator
)


class BuilderValidator(Validator[Builder]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a not null and a Builder object

    # PROVIDES:
      ValidationResult[Builder] containing either:
            - On success: Builder in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Builder]:
        """
        # Action:
            1.  Confirm the candidate is not null and a Builder instance.

        # Parameters:
            *   candidate (Any)

        # Returns:
          BuildResult[Builder] containing either:
                - On success: Builder in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullBuilderException
            *   UnreliableBuilderException
        """
        method = "BuilderValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullBuilderException(f"{method}: {NullBuilderException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not a Builder validation has failed.
            if not isinstance(candidate, Builder):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Builder, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed cast candidate and return in the validation result.
            return ValidationResult.success(cast(Builder, candidate))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an UnreliableBuilderException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            ValidationResult.failure(
                UnreliableBuilderException(ex=ex, message=f"{method}: {UnreliableBuilderException.DEFAULT_MESSAGE}")
            )