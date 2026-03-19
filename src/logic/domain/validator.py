# src/logic/points/coord_stack_validator.py

"""
Module: logic.points.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""


from typing import Any, cast

from logic.square import SquareValidationProcess
from logic.system import IdValidationProcess, LoggingLevelRouter, ValidationProcess, ValidationResult
from logic.domain import (
    Domain, DomainOriginValidationProcess, InvalidDomainException, NullDomainException, DomainNullEnemiesDictException,
    DomainNullFriendsDictException, DomainNullSquaresListException,
)


class DomainValidationProcess(ValidationProcess[Domain]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Domain instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   ValidationProcess

    # PROVIDES:
        * DomainValidationProcess


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            domain_origin_validator: type[DomainOriginValidationProcess] = DomainOriginValidationProcess,
    ) -> ValidationResult[Domain]:
        """
        # ACTION:
        Run checks verifying a candidate is a valid Domain object meeting the minimum requirements
        for use in the system.

        # PARAMETERS:
          * candidate (Any): Object to verify is a Domain.
          * domain_origin_validator (type[DomainOriginValidationProcess]): verifies the DomainOrigin.

        # RETURNS:
          ValidationResult[Domain] containing either:
                - On success: Square in the payload.
                - On failure: Exception.

        Raises:
            * TypeError
            * NullDomainException
            * DomainNullSquaresListException
            * DomainNullEnemiesDictException
            * DomainNullFriendsDictException
            * InvalidDomainException
        """
        method = "DomainValidationProcess.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainException(f"{method}: {NullDomainException.MSG}")
                )
            
            if not isinstance(candidate, Domain):
                return ValidationResult.failure(
                    TypeError(f"{method}: Was expecting type {Domain}, got {type(candidate)} instead")
                )
            
            domain = cast(Domain, candidate)
            
            id_validation = IdValidationProcess.execute(domain.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            domain_origin_validation = domain_origin_validator.execute(domain.origin)
            if domain_origin_validation.is_failure():
                return ValidationResult.failure(domain_origin_validation.exception)
      
            if domain.squares is None:
                return ValidationResult.failure(
                    DomainNullSquaresListException(
                        f"{method}: {DomainNullSquaresListException.MSG}"
                    )
                )
            
            if domain.enemies is None:
                return ValidationResult.failure(
                    DomainNullEnemiesDictException(
                        f"{method}: {DomainNullEnemiesDictException.MSG}"
                    )
                )
            
            if domain.friends is None:
                return ValidationResult.failure(
                    DomainNullFriendsDictException(
                        f"{method}: {DomainNullFriendsDictException.MSG}"
                    )
                )
            
            return ValidationResult.success(domain)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidDomainException(f"{method}: {InvalidDomainException.MSG}", e)
            )
