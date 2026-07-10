# src/validator/endpoint/destination/validator.py

"""
Module: validator.endpoint.destination.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bootstrapper import DestinationCertifierBootstrapper
from err import TokenDestinationCertifierException
from model import Square, Token
from result import ValidationResult
from util import LoggingLevelRouter


class TokenDestinationCertifier:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Certifies a token can end its maneuver at the destination.
        2.  Prevents circular square visits. 

    Attributes:

    Provides:
        -   def validate(
                    token: Token,
                    square: Square,
                    bootstrapper: DestinationCertifierBootstrapper,
            ) -> ValidationResult[Square]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            token: Token,
            destination: Square,
            bootstrapper: DestinationCertifierBootstrapper | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Token is not already in a Square it wants to visit.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   The token is either fully or partially bound to the destination.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            destination: Square
            bootstrapper: DestinationValidatorBootstrapper
        Returns:
            ValidationResult[Square]
        Raises:
            TokenDestinationCertifierException
        """
        method = f"{self.__class__.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if bootstrapper is None:
            bootstrapper = DestinationCertifierBootstrapper()
            
        # Handle the case that, the square is not certified as a destination
        validation_result = bootstrapper.execute(token=token, destination=destination)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDestinationCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDestinationCertifierException.MSG,
                    err_code=TokenDestinationCertifierException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(destination)