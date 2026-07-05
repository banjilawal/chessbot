# src/validation/endpoint/origin/validator.py

"""
Module: validation.endpoint.origin.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrap import OriginCertifierBootstrapper
from err import TokenOriginCertifierException
from model import Square, Token
from result import ValidationResult
from toolkit import TokenEndpointRelationToolkit
from util import LoggingLevelRouter


class TokenOriginCertifier:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Verify a Token has a fully bidirectional relation with the Square it wants
            to travel from

    Attributes:

    Provides:
        -   def validate(
                    token: Token,
                    origin: Square,
                    toolkit: TokenEndpointRelationToolkit
                    bootstrapper: TokenEndpointRelationBootstrapper,
            ) -> ValidationResult[Square]:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            token: Token,
            origin: Square,
            toolkit: TokenEndpointRelationToolkit | None = None,
            bootstrapper: OriginCertifierBootstrapper | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Maneuver's origin contains the right token.

        Action:
            1.  Send an exception chan in the validation result if the token
                is not at the square. Otherwise, send the success result.
        Args:
            token: Token
            origin: Square
            toolkit: TokenEndpointRelationToolkit
            bootstrapper: OriginCertifierBootstrapper
        Returns:
            ValidationResult
        Raises:
            TokenOriginCertifierException
            TokenOriginRelationNullException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenEndpointRelationToolkit()
        if bootstrapper is None:
            bootstrapper = OriginCertifierBootstrapper()
            
        # Handle the case that, the Token has a different origin.
        validation_result = bootstrapper.validate(
            token=token,
            origin=origin,
            toolkit=toolkit,
        )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenOriginCertifierException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginCertifierException.MSG,
                    err_code=TokenOriginCertifierException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(origin)