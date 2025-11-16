# src/chess/domain/validator.py

"""
Module: chess.domain.validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""


from typing import Any, cast

from chess.square import SquareValidator
from chess.system import IdValidator, LoggingLevelRouter, Validator, ValidationResult
from chess.domain import (
    Domain, DomainOriginValidator, InvalidDomainException, NullDomainException, DomainNullEnemiesDictException,
    DomainNullFriendsDictException, DomainNullSquaresListException,
)


class DomainValidator(Validator[Domain]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is a Domain instance that can be used safely in the system.
    
    # PROVIDES:
      ValidationResult[Domain] containing either:
            - On success: Domain in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            domain_origin_validator: type[DomainOriginValidator] = DomainOriginValidator,
    ) -> ValidationResult[Domain]:
        """
        # Action:
        Run checks verifying a candidate is a valid Domain object meeting the minimum requirements
        for use in the system.

        # Parameters:
          * candidate (Any): Object to verify is a Domain.
          * domain_origin_validator (type[DomainOriginValidator]): verifies the DomainOrigin.

        # Returns:
          ValidationResult[Domain] containing either:
                - On success: Square in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * NullDomainException
            * DomainNullSquaresListException
            * DomainNullEnemiesDictException
            * DomainNullFriendsDictException
            * InvalidDomainException
        """
        method = "DomainValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainException(f"{method}: {NullDomainException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Domain):
                return ValidationResult.failure(
                    TypeError(f"{method}: Was expecting type {Domain}, got {type(candidate)} instead")
                )
            
            domain = cast(Domain, candidate)
            
            id_validation = IdValidator.validate(domain.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            domain_origin_validation = domain_origin_validator.validate(domain.origin)
            if domain_origin_validation.is_failure():
                return ValidationResult.failure(domain_origin_validation.exception)
      
            if domain.squares is None:
                return ValidationResult.failure(
                    DomainNullSquaresListException(
                        f"{method}: {DomainNullSquaresListException.DEFAULT_MESSAGE}"
                    )
                )
            
            if domain.enemies is None:
                return ValidationResult.failure(
                    DomainNullEnemiesDictException(
                        f"{method}: {DomainNullEnemiesDictException.DEFAULT_MESSAGE}"
                    )
                )
            
            if domain.friends is None:
                return ValidationResult.failure(
                    DomainNullFriendsDictException(
                        f"{method}: {DomainNullFriendsDictException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(domain)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidDomainException(f"{method}: {InvalidDomainException.DEFAULT_MESSAGE}", e)
            )
