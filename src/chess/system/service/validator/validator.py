# src/chess//service/validator.py

"""
Module: chess..service.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast


from chess.system import LoggingLevelRouter, Service, ValidationResult, Validator


class ServiceValidator(Validator[Service]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is a Service whose Builder, Validator.

    # PROVIDES:
      ValidationResult[Service] containing either:
            - On success: Service in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Service]:
        """
        # Action:
            1.  Confirm the candidate is not null and an Service instance.
            2.  Certify it has a not null Builder
            3.  Certify it has a not null Validator
            4.  Certify it has a not null Finder

        # Parameters:
            *   candidate (Any)

        # Returns:
          BuildResult[Service] containing either:
                - On success: Service in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullServiceException
            *   MissingBuilderException
            *   MissingValidatorException
            *   InvalidServiceException
        """
        method = "ServiceValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullServiceException(f"{method}: {NullServiceException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an  validation has failed.
            if not isinstance(candidate, Service):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Service, got {type(candidate).__name__} instead.")
                )
            
            # Once the two existence checks are passed cast candidate to an Service
            # For additional processing.
            service = cast(Service, candidate)
            
            # Only need to make sure builder is a not-null Builder instance.
            if service.entitt is None or not isinstance(service.builder, Factory):
                return ValidationResult.failure(
                    MissingBuilderException(
                        f"{method}: {MissingBuilderException.DEFAULT_MESSAGE}"
                    )
                )
            # Make sure validator is a not-null Validator instance.
            if service.validator is None or not isinstance(service.validator, Validator):
                return ValidationResult.failure(
                    MissingValidatorException(
                        f"{method}: {MissingValidatorException.DEFAULT_MESSAGE}"
                    )
                )

            # If all checks pass return the Service.
            return ValidationResult.success(service)
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidServiceException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            ValidationResult.failure(
                InvalidServiceException(
                    ex=ex, message=f"{method}: {InvalidServiceException.DEFAULT_MESSAGE}"
                )
            )