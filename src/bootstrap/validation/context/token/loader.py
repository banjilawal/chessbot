# src/bootstrap/validation/context/token/loader.py

"""
Module: bootstrap.validation.context.token.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, TokenValidatorToolkit
from domain import Token, TokenBlueprint, TokenContextPrimeExtract
from err import (
    TokenCarrierEmptyException, TokenContextValidationLoaderException, TokenContextValidationRequestNullException
)
from exchange import TokenContextValidationRequest
from transit import TokenCarrier

from util import LoggingLevelRouter


class TokenContextValidationLoader(ContextValidationLoader[TokenContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TokenContextValidationRequest
            -   TokenCarrier
            -   TokenBlueprint

    Attributes:
        toolkit: TokenValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TokenContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TokenContextPrimeExtract]:
        """
        Extract the TokenBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TokenValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TokenCarrier
                        -   An empty TokenCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a TokenContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenContextPrimeExtract]
        Raises:
            TokenLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=TokenContextValidationRequest,
            null_exception=TokenContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[TokenContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(TokenContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TokenContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)