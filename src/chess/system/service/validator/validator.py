# src/chess/service/validator.py

"""
Module: chess.service.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.system import (
    BuilderValidator, EntityService, LoggingLevelRouter, ValidationResult, Validator, ValidatorCertifier
)
from chess.system.service.exception import Invalidentity_serviceException, NullServiceException
from chess.system.validate.validator import T


class ServiceValidator(Validator[EntityService]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure an EntityService is not null and the correct before use.
    2.  Certify the EntityService's builder and validator are not null and the correct type.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * ServiceValidator

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
    ) -> ValidationResult[EntityService]:
        """
        # Action:
            1.  Confirm the candidate is not null and a Service instance.
            2.  Certify the builder with builder_validator.
            3.  certify the validator with validator_certifier.
            4.  If no checks
            return the exception otherwise, return the certified service
                        in a ValidationResult's payload.
        
        # Parameters:
                    *   candidate (Any)
        
        # Returns:
          ValidationResult[EntityService] containing either:
                - On success: EntityService in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullServiceException
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
            if not isinstance(candidate, EntityService):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Service, got {type(candidate).__name__} instead.")
                )
            
            # Once the two existence checks are passed cast candidate to an Service
            # For additional processing.
            service = cast(EntityService, candidate)
            
            # Only need to make sure builder is a not-null Builder instance.
            builder_certification = builder_validator.validate(service.entity_builder)
            if builder_certification.is_failure():
                return ValidationResult.failure(builder_certification.exception)
            
            validator_certification = validator_certifier.certify(service.entity_validator)
            if validator_certification.is_failure():
                return ValidationResult.failure(validator_certification.exception)

            # If all checks pass return the Service.
            return ValidationResult.success(service)
        
        # Finally, catch any missed exception, wrap an Invalidentity_serviceException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            ValidationResult.failure(
                Invalidentity_serviceException(
                    ex=ex, message=f"{method}: {Invalidentity_serviceException.DEFAULT_MESSAGE}"
                )
            )