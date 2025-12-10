# src/chess/validate/certifier.py

"""
Module: chess..validate.certifier
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    Validator, UnreliableValidatorException, LoggingLevelRouter, NullValidatorException, ValidationResult,
)


class ValidatorCertifier:
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is a not null and a Validator object

    # PROVIDES:
      ValidationResult[Validator] containing either:
            - On success: Validator in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def certify(cls, candidate: Any) -> ValidationResult[Validator]:
        """
        # Action:
            1.  Confirm the candidate is not null and a Validator instance.

        # Parameters:
            *   candidate (Any)

        # Returns:
          BuildResult[Validator] containing either:
                - On success: Validator in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullValidatorException
            *   UnreliableValidatorException
        """
        method = "ValidatorValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullValidatorException(f"{method}: {NullValidatorException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not a Validator validation has failed.
            if not isinstance(candidate, Validator):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Validator, got {type(candidate).__name__} instead.")
                )
            
            # Once the two existence checks are passed cast candidate and return in the validation result.
            return ValidationResult.success(cast(Validator, candidate))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an UnreliableValidatorException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            ValidationResult.failure(
                UnreliableValidatorException(
                    ex=ex, message=f"{method}: {UnreliableValidatorException.DEFAULT_MESSAGE}"
                )
            )